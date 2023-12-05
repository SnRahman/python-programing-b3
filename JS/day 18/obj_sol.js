let student_info = [
    {
        name : 'Ahamd',
        age : 18,
        reg_no : 'AB1233',
        course : 'Python Programing',
        fvrt_pro_lang : ['HTML','CSS','PYTHON','JAVASCRIPT'],
        marks : {
            maths : 90,
            english : 75,
            science : 85,
            urdu : 75,
            Islamic_studies : 90
        }
    },
    {
        name : 'Adeel',
        age : 19,
        reg_no : 'AB1234',
        course : 'Web Programing',
        fvrt_pro_lang : ['HTML','CSS','PHP'],
        marks : {
            maths : 80,
            english : 85,
            science : 90,
            urdu : 81,
            Islamic_studies : 83
        }
    }
]

console.log(student_info)
console.log(student_info[0])
console.log(student_info[1])
console.log('Name : ' + student_info[1].name)
console.log('Age : ' + student_info[1].age)
console.log('Registraion # : ' +student_info[1].reg_no)
console.log('Course : ' +student_info[1].course)
console.log('Fvaroute Programing Languages : ' +student_info[1].fvrt_pro_lang)
console.log('Marks : ')
console.log('Maths : ' + student_info[1].marks.maths)
console.log('English : ' + student_info[1].marks.english)
console.log('Science : ' + student_info[1].marks.science)
console.log('Urdu : ' + student_info[1].marks.urdu)
console.log('Islamic Studies : ' + student_info[1].marks.Islamic_studies)

// 
let fpl_length = student_info[1].fvrt_pro_lang.length
// console.log(fpl_length)
console.log('Fvaroute Programing Languages ')
console.log('First: ' + student_info[1].fvrt_pro_lang[0] )
console.log('Last: ' +student_info[1].fvrt_pro_lang[ fpl_length - 1 ] )


