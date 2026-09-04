import sys
import pandas as pd


def parse_vcf(vcf_file):
    rows = []
    with open(vcf_file) as f:
        for line in f:
            if line.startswith("##") or line.startswith("#CHROM"):
                continue
            fields = line.strip().split("\t")
            chrom, pos, _id, ref, alt, qual, _filter, info = fields[:8]
            is_indel = "INDEL" in info
            dp = None
            for entry in info.split(";"):
                if entry.startswith("DP="):
                    dp = int(entry.split("=")[1])
            rows.append({
                "chrom": chrom, "pos": int(pos), "ref": ref, "alt": alt,
                "qual": float(qual), "type": "INDEL" if is_indel else "SNP",
                "depth": dp,
            })
    return pd.DataFrame(rows)


def summarize(vcf_file):
    df = parse_vcf(vcf_file)
    print(f"Total variants: {len(df)}")
    print(f"SNPs: {(df['type'] == 'SNP').sum()}")
    print(f"Indels: {(df['type'] == 'INDEL').sum()}")
    print(f"Average quality: {df['qual'].mean():.2f}")
    print(f"Average depth: {df['depth'].mean():.2f}")
    df.to_csv("variant_summary.csv", index=False)
    print("Saved to variant_summary.csv")


if __name__ == "__main__":
    vcf_path = sys.argv[1] if len(sys.argv) > 1 else "variants.vcf"
    summarize(vcf_path)
