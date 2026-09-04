# E. coli Variant Calling Pipeline

A command-line bioinformatics pipeline that aligns paired-end sequencing
reads to a reference genome and identifies genetic variants (SNPs and
indels) using BWA, samtools, and bcftools.

## Workflow
Raw FASTQ reads -> BWA index -> BWA mem alignment -> samtools sort/index
-> bcftools mpileup -> bcftools call -> variants.vcf

## Setup
conda env create -f environment.yml
conda activate variant-calling

## Usage
bash run_pipeline.sh
python summarize_vcf.py variants.vcf

## Results
- 350,000 paired-end reads aligned to E. coli REL606 reference genome
- 99.98% mapping rate, 99.05% properly paired
- Real SNPs and indels identified and summarized

## Tech stack
BWA, samtools, bcftools, Python, pandas, conda
