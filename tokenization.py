import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print('vocab size: ', encoder.n_vocab)


text = 'The cat sat on the met'

print(encoder.encode(text)) #[976, 9059, 10139, 402, 290, 1421]

text2 = 'The cat sat on the met.'

print(encoder.encode(text2))  #[976, 9059, 10139, 402, 290, 1421, 13]

print('decoded->', encoder.decode([976, 9059, 10139, 402, 290, 1421])) # decoded-> The cat sat on the met