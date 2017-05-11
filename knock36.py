# coding: UTF-8

# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

def Create_freq_dict(data_path):

    import knock30
    result = knock30.morpho(data_path)

    freq_dict = {}
    for sentence in result:
        for word_dict in sentence:
            if word_dict['base'] in freq_dict:
                freq_dict[word_dict['base']] += 1
            else:
                freq_dict[word_dict['base']] = 1
    return freq_dict



if __name__ == '__main__':

    freq_dict = Create_freq_dict("documents/neko.mecab")
    for key, value in sorted(freq_dict.items(), key=lambda x:x[1], reverse=True):
        print key,value
