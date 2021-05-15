# Replace UnknownGenes

当我使用ucsc的get2bed工具（gtfToGenePred + genePredToBed）转换gtf文件为bed12文件时，碰到如下错误:

```
invalid gffGroup detected on line: NC_001137.3  RefSeq  stop_codon      375215  375217  0.000000        -       0       gene_id "YER109C"; transcript_id "unknown_transcript_1";
GFF/GTF group unknown_transcript_1 on NC_001136.10-, this line is on NC_001137.3-, all group members must be on same seq and strand
```

原因是因为在gtf文件第9列中含有多个transcript_id相同的记录，都为unknown_transcript_1：如下所示

```
NC_001136.10    RefSeq  CDS     721074  721481  .       -       0       gene_id "YDR134C"; transcript_id "unknown_transcript_1"; db_xref "SGD:S000002541"; db_xref "GeneID:851712"; experiment "EXISTENCE:direct assay:GO:0009277 fungal-type cell wall [PMID:10383953]"; gbkey "CDS"; gene "CCW22"; locus_tag "YDR134C"; note "Cell wall protein; YDR134C has a paralog, CCW12, that arose from the whole genome duplication; S. cerevisiae genome reference strain S288C contains an internal in-frame stop at codon 67, which in other strains encodes glutamine";
NC_001136.10    RefSeq  start_codon     721479  721481  .       -       0       gene_id "YDR134C"; transcript_id "unknown_transcript_1"; db_xref "SGD:S000002541"; db_xref "GeneID:851712"; experiment "EXISTENCE:direct assay:GO:0009277 fungal-type cell wall [PMID:10383953]"; gbkey "CDS"; gene "CCW22"; locus_tag "YDR134C"; note "Cell wall protein; YDR134C has a paralog, CCW12, that arose from the whole genome duplication; S. cerevisiae genome reference strain S288C contains an internal in-frame stop at codon 67, which in other strains encodes glutamine";
NC_001136.10    RefSeq  stop_codon      721071  721073  .       -       0       gene_id "YDR134C"; transcript_id "unknown_transcript_1"; db_xref "SGD:S000002541"; db_xref "GeneID:851712"; experiment "EXISTENCE:direct assay:GO:0009277 fungal-type cell wall [PMID:10383953]"; gbkey "CDS"; gene "CCW22"; locus_tag "YDR134C"; note "Cell wall protein; YDR134C has a paralog, CCW12, that arose from the whole genome duplication; S. cerevisiae genome reference strain S288C contains an internal in-frame stop at codon 67, which in other strains encodes glutamine";
NC_001224.1     RefSeq  CDS     13818   13986   .       +       0       gene_id "Q0060"; transcript_id "unknown_transcript_10"; experiment "EXISTENCE:direct assay:GO:0004519 endonuclease activity [PMID:7797552]"; gbkey "CDS"; gene "AI3"; locus_tag "Q0060"; note "Endonuclease I-SceIII; encoded by a mobile group I intron within the mitochondrial COX1 gene"; product "intron-encoded DNA endonuclease aI3"; protein_id "NP_009308.2"; transl_table "3";
NC_001224.1     RefSeq  CDS     16435   16470   .       +       2       gene_id "Q0060"; transcript_id "unknown_transcript_10"; experiment "EXISTENCE:direct assay:GO:0004519 endonuclease activity [PMID:7797552]"; gbkey "CDS"; gene "AI3"; locus_tag "Q0060"; note "Endonuclease I-SceIII; encoded by a mobile group I intron within the mitochondrial COX1 gene"; product "intron-encoded DNA endonuclease aI3"; protein_id "NP_009308.2"; transl_table "3";
```

而ucsc的 gtfToGenePred 软件认为你这些都是同一个转录本，但是在不同的染色体的不同位置。所以程序报错，说同一个转录本必须是在相同的链上，相同的序列。

解决办法是，将这些都为`unknown_transcript_1`的记录按照是否是同一个基因进行人为分组。gene_id相同的转录本设置为同一个编号，基因不同的转录本设置为递增的编号。

```
unknown_transcript_1
unknown_transcript_2
unknown_transcript_3
unknown_transcript_4
......
```