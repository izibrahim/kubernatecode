#word count

phars = '''
 CKA  POD

Checking the POD status

kubectl get POD

Creating POD with image nginx

kubectl run nginx imagenginx

Counting the POD

Note noheaders remove the header & wc l will count the lines

kubectl get POD noheaders | wc l

Checking the image in the POD


kubectl describe POD | grep  Image
kubectl  describe POD webapp |  grep State

Checking the POD running on which Nodes


kubectl  get POD o wide

Delete the POD


kubectl delete POD webapp

Create the POD using the definition file it will not create the POD but create the definition file


kubectl run redis imageredis123 dryrunclient o yaml > POD.yml
 Create the POD now
kubectl apply f POD.yml

Change the Image of running POD

vi POD.yml
use vi and change the image

vi
vi
'''

#print(phars)


split_word = phars.split()
#print(split_word)

convert_to_set = set(split_word)
#print(convert_to_set)

#print(convert_dict)

new_dict = dict()
value = 1
for count_word in convert_to_set:
    count_word = count_word.lower()
    for word_count  in  split_word:
        word_count = word_count.lower()
        if count_word in  word_count:
           new_dict[count_word] = value
           value = value + 1
    value = 1

print(new_dict)
