import os

path = 'GCF_000146045.2_R64_genomic.gtf'
path2 = 'GCF_000146045.2_R64_genomic_replace.gtf'

fh = open(path, 'r+')
fp = open(path2, 'w+')

# linux commands
# cat GCF_000146045.2_R64_genomic.gtf | grep 'unknown_transcript_1' | cut -f 9 | cut -d ';' -f 1 | cut -d ' ' -f 2 | uniq | tr '\n' ','

gene_id_list=["YDR134C","YER109C","YIL167W","YIR043C","YOL153C","YOR031W","Q0045","Q0070","Q0065","Q0060","Q0055","Q0050","Q0075","Q0080","Q0085","Q0105","Q0120","Q0115","Q0110","Q0130","Q0140","Q0160","Q0250","Q0255","Q0275"]
gene_id_dic = dict(zip(gene_id_list,[i for i in range(1,len(gene_id_list)+1)]))

transcript_id_unknown = 'unknown_transcript_1'

for eachLine in fh.readlines():
    if eachLine.__contains__("unknown_transcript_1"):
        arr = eachLine.split('\t')
        arr2 = arr[8].split(';')
        arr3 = arr2[0].split()
        arr4 = arr2[1].split()
        gene_id = eval(arr3[1])
        transcript_id = eval(arr4[1])
        count = str(gene_id_dic[gene_id])
        transcript_id_unknown_bak = "unknown_transcript_"+count
        print(transcript_id_unknown_bak)
        eachLine = eachLine.replace(transcript_id_unknown, transcript_id_unknown_bak)
        print(eachLine)
        fp.write(eachLine)
    else:
        fp.write(eachLine)
fh.close()
fp.close()