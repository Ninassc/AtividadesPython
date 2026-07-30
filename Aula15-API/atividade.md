PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json" `
>> -Body '{"titulo":"Dom Casmurro","autor":"Machado de Assis","ano":1899}'


ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-30 08:07:31.534910
id           : 4
titulo       : Dom Casmurro



PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json" `
>> -Body '{"titulo":"O Alquimista","autor":"Paulo Coelho","ano":1988}'


ano          : 1988
autor        : Paulo Coelho
data_criacao : 2026-07-30 08:08:11.098332
id           : 5
titulo       : O Alquimista



PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json" `
>> -Body '{"titulo":"Ensaio Sobre a Cegueira","autor":"José Saramago","ano":1995}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe9 in position 48: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json" `
>> -Body '{"titulo":"Ensaio Sobre a Cegueira","autor":"José Saramago","ano":1995}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe9 in position 48: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json;charset=utf-8" `
>> -Body '{"titulo":"Ensaio Sobre a Cegueira","autor":"José Saramago","ano":1995}'


ano          : 1995
autor        : José Saramago
data_criacao : 2026-07-30 08:10:13.019232
id           : 6
titulo       : Ensaio Sobre a Cegueira



PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json;charset=utf-8" `
>> -Body '{"titulo":"Capitães da Areia","autor":"Jorge Amado","ano":1937}'
>>


ano          : 1937
autor        : Jorge Amado
data_criacao : 2026-07-30 08:10:20.512091
id           : 7
titulo       : Capitães da Areia



PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json;charset=utf-8" `
>> -Body '{"titulo":"Vidas Secas","autor":"Graciliano Ramos","ano":1938}'


ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-30 08:10:28.850468
id           : 8
titulo       : Vidas Secas



PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json;charset=utf-8" `
>> -Body '{"titulo":"Grande Sertão: Veredas","autor":"João Guimarães Rosa","ano":1956}'
>>


ano          : 1956
autor        : João Guimarães Rosa
data_criacao : 2026-07-30 08:10:35.833607
id           : 9
titulo       : Grande Sertão: Veredas



PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json;charset=utf-8" `
>> -Body '{"titulo":"A Hora da Estrela","autor":"Clarice Lispector","ano":1977}'


ano          : 1977
autor        : Clarice Lispector
data_criacao : 2026-07-30 08:10:42.372986
id           : 10
titulo       : A Hora da Estrela



PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> -Method POST `
>> -ContentType "application/json;charset=utf-8" `
>> -Body '{"titulo":"O Cortiço","autor":"Aluísio Azevedo","ano":1890}'


ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-30 08:10:48.069203
id           : 11
titulo       : O Cortiço

PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
>>    -Method PUT `
>>    -ContentType "application/json;charset=utf-8" `
>>    -Body '{"titulo":"O Senhor dos Anéis","autor":"J. R. R. Tolkien","ano":1954}'
>>


ano          : 1954
autor        : J. R. R. Tolkien
data_criacao : 2026-07-30 08:07:31.534910
id           : 4
titulo       : O Senhor dos Anéis

PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 -Method DELETE

PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 -Method DELETE

PS C:\Users\22403000> Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 -Method DELETE