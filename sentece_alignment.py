#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


res_list_con = []
res_list_spl = []
res_list_typo = []


# In[3]:


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


# In[4]:


def cosine(first, second):

    ln = len(first)
    if len(second) > ln:
        ln = len(second)
    count = 0
    for c1 in first:
        ind = second.find(c1)
        if ind != -1:
            count = count+1
            h1 = second[0:ind]
            h2 = second[ind+1:len(second)]
            second = h1+h2

    return count/float(ln)


# In[5]:


def replace_list(text, r_list, c):
    for r in r_list:
            text = text.replace(r, c)
    return text


# In[6]:


'''
def preprocess(s):
    #s = re.sub(' +', ' ', s)
    s = s.replace("."," ").replace(","," ").replace("?"," ").replace("!"," ").replace("\"","").replace("-","").replace("("," ").replace(")"," ").replace(";"," ").replace(":"," ").replace("/"," ").replace("+"," ").replace("%"," ").replace("_"," ").replace("&", " ").replace("[", " ").replace("]", " ").replace("#", " ")
    s = s.replace("~", "").replace("*", "").replace("<", "").replace(">", "").replace("^", "").replace("¦", "")
    s = s.replace("´", "'")
    s = s.replace("À", "A").replace("Â", "A").replace("Ä", "A").replace("", "A").replace("")
    s = s.replace("È","E").replace("É", "E").replace("Ê", "E").replace("Ë", "E")
    s = s.replace("Ì", "İ").replace("Í", "İ").replace("Î", "İ").replace("Ï", "İ")
    s = s.replace("Ñ", "N")
    s = s.replace("Ò", "Ö").replace("Ô", "Ö").replace("Õ", "Ö")
    s = s.replace("Ù", "Ü").replace("Ú", "Ü").replace("Û", "Ü")
    s = s.replace("×", "X")
    s = re.sub(" \d+", " ", s)
    s = re.sub(' +', ' ', s).strip()

    return s
'''


# In[7]:


def preprocess(s):
    a = ["Å", "Ǻ", "Ḁ", "Ă", "Ặ", "Ắ", "Ằ", "Ẳ", "Ẵ", "Ȃ", "Â", "Ậ", "Ấ", "Ầ", "Ẫ", "Ẩ", "Ả", "Ǎ", "Ⱥ", "Ȧ", "Ǡ", "Ạ", "Ä", "Ǟ", "À", "Ȁ", "Á", "Ā", "Ã", "Ą"]
    _c = ["Ć", "Ĉ", "Č", "Ċ", "Ḉ", "Ƈ", "Ȼ", "Ç"]
    e = ["Ĕ", "Ḝ", "Ȇ", "Ê", "Ề", "Ế", "Ể", "Ễ", "Ệ", "Ẻ", "Ḙ", "Ě", "Ɇ", "Ė", "Ẹ", "Ë", "È", "Ȅ", "É", "Ē", "Ḕ", "Ḗ", "Ẽ", "Ḛ", "Ę", "Ȩ"]
    i = ["i̇".upper(), "İ", "Ị", "Ĭ", "Î", "Ǐ", "Ɨ", "Ï", "Ḯ", "Í", "Ì", "Ȉ", "Į", "Ī", "ᶖ", "Ỉ", "Ȋ", "Ĩ", "Ḭ"]
    _u = ["Ŭ", "Ǜ", "Ǘ", "Ǚ", "Ǖ", "Ú", "Ù", "Û", "Ǔ", "Ȗ", "Ű", "Ư", "Ứ", "Ừ", "Ử", "Ự", "Ữ", "Ủ", "Ū", "Ṻ", "Ũ", "Ṹ", "Ȕ", "Ů"]
    _o = ["Ȫ", "Ó", "Ò", "Ô", "Ố", "Ồ", "Ổ", "Ỗ", "Ộ", "Ǒ", "Ő", "Ŏ", "Ȏ", "Ȯ", "Ȱ", "Ọ", "Ɵ", "Ơ", "Ớ", "Ờ", "Ỡ", "Ợ", "Ở", "Ỏ", "Ō", "Ṓ", "Ṑ", "Õ", "Ȭ", "Ṍ", "Ṏ", "Ǫ", "Ȍ", "Ǭ"]
    _s = ["Ś", "Ṡ", "Ṩ", "Ṥ", "Ꞩ", "Ŝ", "Ṧ", "Š", "Ş", "Ș", "ᶊ", "Ȿ", "ᵴ", "ᶳ"]
    n = ["Ń", "Ñ", "Ň", "Ǹ", "Ṅ", "Ṇ", "Ņ", "Ṉ", "Ṋ", "Ꞥ", "ᵰ", "ᶇ"]
    
    '''
    a = ["å","ǻ","ḁ","ă","ặ","ắ","ằ","ẳ","ẵ","ȃ","â","ậ","ấ","ầ","ẫ","ẩ","ả","ǎ","ⱥ","ȧ","ǡ","ạ","ä","ǟ","à","ȁ","á","ā","ã","ą"]
    _c = ["ć","ĉ","č","ċ","ḉ","ƈ","ȼ","ç"]
    e = ["ĕ","ḝ","ȇ","ê","ề","ế","ể","ễ","ệ","ẻ","ḙ","ě","ɇ","ė","ẹ","ë","è","ȅ","é","ē","ḕ","ḗ","ẽ","ḛ","ę","ȩ"]
    i = ["i̇", "i̇","i̇","ị","ĭ","î","ǐ","ɨ","ï","ḯ","í","ì","ȉ","į","ī","ᶖ","ỉ","ȋ","ĩ","ḭ"]
    _u = ["ŭ","ǜ","ǘ","ǚ","ǖ","ú","ù","û","ǔ","ȗ","ű","ư","ứ","ừ","ử","ự","ữ","ủ","ū","ṻ","ũ","ṹ","ȕ","ů"]
    _o = ["ȫ","ó","ò","ô","ố","ồ","ổ","ỗ","ộ","ǒ","ő","ŏ","ȏ","ȯ","ȱ","ọ","ɵ","ơ","ớ","ờ","ỡ","ợ","ở","ỏ","ō","ṓ","ṑ","õ","ȭ","ṍ","ṏ","ǫ","ȍ","ǭ"]
    _s = ["ś","ṡ","ṩ","ṥ","ꞩ","ŝ","ṧ","š","ş","ș","ᶊ","ȿ","ᵴ","ᶳ"]
    n = ["ń","ñ","ň","ǹ","ṅ","ṇ","ņ","ṉ","ṋ","ꞥ","ᵰ","ᶇ"]
    '''
    
    x = ["×"]
    aps = ["`", "´"]

    remove = ["~", "*", "<", ">", "^", "¦", "€", "$", "£"]
    space = [".", ",", ";", ":", "?", "!", "\"", "(", ")", "[", "]", "/", "+", "-", "_", "#", "%", "&", "|"]
    
    s = replace_list(s, a, "a")
    s = replace_list(s, _c, "ç")
    s = replace_list(s, e, "e")
    s = replace_list(s, i, "i")
    s = replace_list(s, n, "n")
    s = replace_list(s, _o, "ö")
    s = replace_list(s, _s, "ş")
    s = replace_list(s, _u, "ü")
    s = replace_list(s, x, "x")
    s = replace_list(s, aps, "'")
    s = replace_list(s, remove, "")
    s = replace_list(s, space, " ")
    
    s = s.replace("İ", "i").replace("I", "ı")
    
    s = re.sub(" \d+", " ", s)
    s = re.sub(" +", " ", s).strip()

    return s


# In[8]:


def get_space_index_list(s):
    space_index_list = []
    count = 0
    for w in s:
        if w == " ":
            space_index_list.append(count)
        count += 1

    return space_index_list


# In[9]:


def remove_character_at(s, index):
    return {'generated_sentecece':s[0: index:] + s[index + 1::], 'original_words':s[0: index:].split()[-1] + " " + s[index + 1::].split()[0]}


# In[10]:


def remove_character_at_v2(s, index):
    return {'generated_sentecece':s[0:index:].split()[-1] + s[index+1:].split()[0], 'original_words':s[0:index:].split()[-1] + " " + s[index+1:].split()[0], 'index':index}


# In[11]:


def generate_grams(s):
    gram_list = []
    space_index_list = get_space_index_list(s)

    for space_index in space_index_list:
        gram_list.append(remove_character_at_v2(s, space_index))

    return gram_list


# In[12]:


def remove_found_words(right_sentece, wrong_sentence, res_list):
    for res in res_list:
        rw = res.split(" - ")[1]
        ww = res.split(" - ")[0]
        right_sentece = re.sub(r'\b' + rw + r'\b', '', right_sentece)
        wrong_sentence = re.sub(r'\b' + ww + r'\b', '', wrong_sentence)

    right_sentece = re.sub(' +', ' ', right_sentece).strip()
    wrong_sentence = re.sub(' +', ' ', wrong_sentence).strip()

    return right_sentece, wrong_sentence


# In[13]:


def get_mistyped_word_list_v2(s2_s, s1_s, n=10):
    s1_s = s1_s.split()
    s2_s = s2_s.split()
    res = []
    current_index = 0
    for s1 in s1_s:

        # just search for -n, +n neighborhood
        #####################################
        f_index = current_index - n
        if f_index < 0:
            f_index = 0
        l_index = current_index + n
        if l_index >= len(s2_s):
            l_index = len(s2_s) - 1
        #####################################
        
        min_change = 0
        min_s2 = ""
        flag = False
        for i in range(f_index, l_index):
            s2 = s2_s[i]
            diff = (abs(s1_s.index(s1) - s2_s.index(s2)) + 1)
            lev = levenshtein(s1, s2) + 1
            cos = cosine(s1, s2)
            score = (1. / (lev * diff))
            # if (lev <= 4 and cos >= 0.7) and score >= 0.25 and score > min_change:
            if ((lev <= 4 and cos >= 0.7) or cos > 0.8) and score > min_change:  # ikinci kosula karakter uzunlugu da ekle
                min_change = score
                min_s2 = s2
                flag = True
        if flag:
            if min_s2 != s1:
                res.append(s1 + " - " + min_s2)
        current_index += 1

    return res


# In[14]:


def get_mis_concatted_word_list_v2(right_sentece, wrong_sentece, n=10):
    gram_list = generate_grams(right_sentece)
    res_list = []
    sen2_list = wrong_sentece.split()
    current_index = 0

    for gram in gram_list:

        space_count = 0
        for str in right_sentece[0:gram['index']+1]:
            if str == " ":
                space_count += 1

        current_index = space_count

        # just search for -n, +n neighborhood
        #####################################
        f_index = current_index - n
        if f_index < 0:
            f_index = 0
        l_index = current_index + n
        if l_index >= len(sen2_list):
            l_index = len(sen2_list) - 1
        #####################################

        max_cos_score = 0
        max_lev_score = 0
        corrected = ""
        wrong = ""

        # for word2 in sen2_list:
        for i in range(f_index, l_index):
            word2 = sen2_list[i]
            cos_score = cosine(gram['generated_sentecece'], word2)
            lev_score = levenshtein(gram['generated_sentecece'], word2)
            if cos_score > max_cos_score:
                corrected = gram['original_words']
                wrong = word2
                max_cos_score = cos_score
                max_lev_score = lev_score
        # if max_lev_score <= 2 and max_cos_score >= 0.85:
        if max_lev_score <= 0 and max_cos_score >= 1:
            res_list.append(wrong + " - " + corrected)
    return res_list


# In[15]:


def get_mis_splitted_word_list_v2(right_sentece, wrong_sentece, n=10):
    gram_list = generate_grams(wrong_sentece)
    res_list = []
    sen2_list = right_sentece.split()
    current_index = 0

    for gram in gram_list:

        space_count = 0
        for str in wrong_sentece[0:gram['index']+1]:
            if str == " ":
                space_count += 1

        current_index = space_count

        # just search for -n, +n neighborhood
        #####################################
        f_index = current_index - n
        if f_index < 0:
            f_index = 0
        l_index = current_index + n
        if l_index >= len(sen2_list):
            l_index = len(sen2_list) - 1
        #####################################

        max_cos_score = 0
        max_lev_score = 0
        corrected = ""
        wrong = ""

        # for word2 in sen2_list:
        for i in range(f_index, l_index):
            word2 = sen2_list[i]
            cos_score = cosine(gram['generated_sentecece'], word2)
            lev_score = levenshtein(gram['generated_sentecece'], word2)
            if cos_score > max_cos_score:
                corrected = gram['original_words']
                wrong = word2
                max_cos_score = cos_score
                max_lev_score = lev_score
        # if max_lev_score <= 2 and max_cos_score >= 0.85:
        if max_lev_score <= 0 and max_cos_score >= 1:
            res_list.append(corrected + " - " + wrong)
    return res_list


# In[16]:


def get_mistyped_word_list(s2_s, s1_s):

    s1_s = s1_s.split()
    s2_s = s2_s.split()
    res = []
    for s1 in s1_s:
        min_change = 0
        min_s2 = ""
        flag = False
        for s2 in s2_s:
            #if s1 == s2:
            #    break
            diff = (abs(s1_s.index(s1) - s2_s.index(s2)) + 1)
            lev = levenshtein(s1, s2) + 1
            cos = cosine(s1, s2)
            score = (1. / (lev * diff))
            # if (lev <= 4 and cos >= 0.7) and score >= 0.25 and score > min_change:
            if ((lev <= 4 and cos >= 0.7) or cos > 0.8) and score > min_change: # ikinci kosula karakter uzunlugu da ekle
                min_change = score
                min_s2 = s2
                flag = True
        if flag:
            if min_s2 != s1:
                res.append(s1 + " - " + min_s2)

    return res


# In[17]:


def get_mis_concatted_word_list(right_sentece, wrong_sentece):
    gram_list = generate_grams(right_sentece)
    res_list = []
    sen2_list = wrong_sentece.split()
    for gram in gram_list:
        max_cos_score = 0
        max_lev_score = 0
        corrected = ""
        wrong = ""
        for word2 in sen2_list:
            cos_score = cosine(gram['generated_sentecece'], word2)
            lev_score = levenshtein(gram['generated_sentecece'], word2)
            if cos_score > max_cos_score:
                corrected = gram['original_words']
                wrong = word2
                max_cos_score = cos_score
                max_lev_score = lev_score
        #if max_lev_score <= 2 and max_cos_score >= 0.85:
        if max_lev_score <= 0 and max_cos_score >= 1:
            res_list.append(wrong + " - " + corrected)
    return res_list


# In[18]:


def get_mis_splitted_word_list(right_sentece, wrong_sentece):
    gram_list = generate_grams(wrong_sentece)
    res_list = []
    sen2_list = right_sentece.split()
    for gram in gram_list:
        max_cos_score = 0
        max_lev_score = 0
        corrected = ""
        wrong = ""
        for word2 in sen2_list:
            cos_score = cosine(gram['generated_sentecece'], word2)
            lev_score = levenshtein(gram['generated_sentecece'], word2)
            if cos_score > max_cos_score:
                corrected = gram['original_words']
                wrong = word2
                max_cos_score = cos_score
                max_lev_score = lev_score
        #if max_lev_score <= 2 and max_cos_score >= 0.85:
        if max_lev_score <= 0 and max_cos_score >= 1:
            res_list.append(corrected + " - " + wrong)
    return res_list


def insert_mis_concat_words(w1, w2):
    return


def insert_mis_splitted_words(w1, w2):
    return


def insert_mistyped_words(w1, w2):
    return



def assign_input_sentences(sen1, sen2, concat_id, count):
    sen1 = preprocess(sen1)
    sen2 = preprocess(sen2)
    res_list_con_ = get_mis_concatted_word_list_v2(sen1, sen2)
    #sen1, sen2 = remove_found_words(sen1, sen2, res_list_con)
    res_list_spl_ = get_mis_splitted_word_list_v2(sen1, sen2)
    #sen1, sen2 = remove_found_words(sen1, sen2, res_list_spl)
    res_list_typ_ = get_mistyped_word_list_v2(sen1, sen2)

    #res_list_con = res_list_con + res_list_con_
    #res_list_spl = res_list_spl + res_list_spl_
    #res_list_typo = res_list_typo + res_list_typo_
    
    #res_list_con_ = list(set(res_list_con_))
    #res_list_spl_ = list(set(res_list_spl_))
    #res_list_typo_ = list(set(res_list_typo_))

        
    file_name__mis_spl = "mis_spl.txt"
    with open(file_name__mis_spl, "a") as myfile_spl:
        for res in res_list_spl_:
            myfile_spl.write(concat_id + "," + str(count) + "," + res.lower() + ",mis_spl\n")

    #file_name__mis_con = "mis_con.txt"
    #with open(file_name__mis_con, "a") as myfile_con:
        for res in res_list_con_:
            myfile_spl.write(concat_id + "," + str(count) + "," + res.lower() + ",mis_con\n")
    
    #file_name__mis_typ = "mis_typ.txt"
    #with open(file_name__mis_typ, "a") as myfile_typ:
        for res in res_list_typ_:
            myfile_spl.write(concat_id + "," + str(count) + "," + res.lower() + ",mis_typ\n")

    #print("*****")
    #print("mis-concatted words : " + str(res_list_con_))
    #print("\n")
    #print("mis-splitted words  : " + str(res_list_spl_))
    #print("\n")
    #print("mis-typed words     : " + str(res_list_typ_))
    #print("*****")

    return



from datameer_api.util import datameer_util as dmu
import pandas as pd

workbook_id = '43454'
sheet_name = 'column_wise'
csv_name = 'sentence_correction.csv'

# indirilen veri; id, dogru cumle, yanlis cumle olacak sekilde iliskisel veri tabanı şeklinde bulunmaktadir
DOWNLOAD_PATH = '/home/jupyter/lib/datameer_api/data/'
dmu.download_workbook_data(workbook_id, sheet_name, csv_name)


df = pd.read_csv(DOWNLOAD_PATH + csv_name)


count = 0
for index, row in df.iterrows():
    assign_input_sentences(row['corrected'].upper(), row['raw'].upper(), row['concat_id'],count)
    count+=1



