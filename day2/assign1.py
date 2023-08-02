def trip(is_sunny, have_money, have_passport):
    if is_sunny and have_money and have_passport:
        print("We will fly to Antalya")
    elif is_sunny and have_money and not have_passport:
        print("We will go to Nablus")
    elif not is_sunny and have_money and  have_passport:
        print("We will fly to Sharm")
    elif not is_sunny and have_money and not have_passport:
        print("We will go to the deadsea")
    else:
        print("I will stay home")
        
trip(True,True, True) # , بدل 11 سطر كتبنا سطر 1
trip(True,False, True) # , بدل 11 سطر كتبنا سطر 1
trip(False,True, True) # , بدل 11 سطر كتبنا سطر 1
trip(False,True, False) # , بدل 11 سطر كتبنا سطر 1
# بدل ما نعدل على كل الملف  4 مرات نعمل التعديل مرة واحدة في داخل الفنكشن 

