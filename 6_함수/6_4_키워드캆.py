def profile(name, age, main_lang): #profile(name, age, main_lang)라는 함수가 생성된다.
    print(name, age, main_lang) #name, age, main_lang[전체로 지정된 변수]가 출력된다.

profile(name="Muchim Doraji", main_lang="한국어, 영어, 스페인어, 포르투갈어, 아랍어", age=166528) #name="Muchim Doraji", main_lang="한국어, 영어, 스페인어, 포르투갈어, 아랍어", age=166528로 지정된다.
profile(main_lang="아랍어, 벵골어, 헝가리어, 베트남어, 러시아어", age=23987178, name="Muchim Gaji") #main_lang="아랍어, 벵골어, 헝가리어, 베트남어, 러시아어", age=23987178, name="Muchim Gaji"로 출력된다.