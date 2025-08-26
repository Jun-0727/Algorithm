from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = defaultdict(list)

for word in words:
    anagrams[''.join(sorted(word))].append(word)


print(anagrams.values())

"""
    1. defaultdict(list) : value를 리스트 형태로 가짐

    2. sorted(문자열)는 문자열을 정렬해서 리스트로 반환

    3. ''.join(리스트)은 리스트 원소를 연결
    
    4. dict.values()는 딕셔너리의 value 값만 추출
"""