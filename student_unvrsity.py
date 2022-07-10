# 1)inrto 2)processing 3)output

# 1)
school_gen_mark = 5.6       #float
university_min_mark = 7.5   #float

sudent_montly_earn = 200   #int
university_contr_cost = 6000    #int/ year
student_powerful_dad = False #True type

# 2)
approve = school_gen_mark >= university_min_mark\
          or\
          sudent_montly_earn * 12 >= university_contr_cost\
          or\
          student_powerful_dad == True

# 3)
print("will the student aproved?", approve )        