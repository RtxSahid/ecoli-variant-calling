#!/bin/bash
set -e

REF="ecoli_rel606.fasta"
READS1="sub/SRR2584866_1.trim.sub.fastq"
READS2="sub/SRR2584866_2.trim.sub.fastq"

echo "STEP 1: Indexing reference genome"
bwa index "$REF"

echo "STEP 2: Aligning reads to reference (BWA)"
bwa mem "$REF" "$READS1" "$READS2" > aligned.sam

echo "STEP 3: Converting, sorting, and indexing alignment"
samtools view -b aligned.sam > aligned.bam
samtools sort aligned.bam -o aligned.sorted.bam
samtools index aligned.sorted.bam
samtools flagstat aligned.sorted.bam

echo "STEP 4: Calling variants (bcftools)"
bcftools mpileup -f "$REF" aligned.sorted.bam -O b -o raw_calls.bcf
bcftools call -mv -O v -o variants.vcf raw_calls.bcf

echo "Done! variants.vcf contains all detected variants."
grep -v "^##" variants.vcf | head -20
