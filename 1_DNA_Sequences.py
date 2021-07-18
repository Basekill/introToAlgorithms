
def longest_subsequence_length(string1,string2):
    sub1 = []
    for i in range(len(string1)):
        for j in range(i+1,len(string1)+1):
            sub1.append(string1[i:j])
    print(sub1)


def test_longest_subsequence_length():
    assert longest_subsequence_length("CCGTCAGTCGCG","TGTTTCGGAATGCAA") == 3

longest_subsequence_length("ABC","ABC")


