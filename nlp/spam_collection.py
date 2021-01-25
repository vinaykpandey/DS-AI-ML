# https://archive.ics.uci.edu/ml/datasets/sms+spam+collection
# Download: Data Folder,
raw_data = open('SMSSpamCollection').read()
raw_data[0:500]

parsed_data = raw_data.replace('\t', '\n').split('\n')
# print(parsed_data)
label_list = parsed_data[0::2]
msg_list = parsed_data[1::2]
print(label_list[:5])
print(msg_list[:5])




# using pandas csv read
df = pd.read_csv('SMSSpamCollection', sep="\t", header=None)
df
df.columns = ['label', 'sms']
# df
# print(len(df.columns), len(df))
ham_df = df[df['label']== "ham"]
print("ham count ", len(ham_df))
spam_df = df[df['label']== "spam"]
print("spam count ", len(spam_df))

missing_label_count = df["label"].isnull().sum()
print("missing_label_count ", missing_label_count)
missing_sms_count = df["sms"].isnull().sum()
print("missing_sms_count ", missing_sms_count)


