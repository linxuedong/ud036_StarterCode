import fresh_tomatoes
from media import Movie

# create movies date
toy_story = Movie('玩具总动员',
                  '牛仔警长胡迪和太空骑警巴斯光年的故事。',
                  'https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=77119894c9fcc3ceb4c0ce35aa7eb1b5/d62a6059252dd42a1835151d023b5bb5c9eab843.jpg',
                  'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = Movie('Avatar',
               'A marine on an alien planet',
               'https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/h%3D152/sign=8e7342b45143fbf2da2ca226827fca1e/9825bc315c6034a816f0df3dc91349540923767f.jpg',
               'https://www.youtube.com/watch?v=5PSNL1qE6VY')

pirates_caribbean = Movie('Pirates of the Caribbean',
                          'Dead Men Tell No Tales',
                          'https://ss1.baidu.com/6OZ1bjeh1BF3odCf/it/u=1598159804,3592535339&fm=20',
                          'https://www.youtube.com/watch?v=XibzC-e_s5M')

school_of_rock = Movie('School Of Rock',
                       'Using rock music to learn',
                       'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3016129913,2142710803&fm=27&gp=0.jpg',
                       'https://www.youtube.com/watch?v=3PsUJFEBC74')

bad_genius = Movie('Bad Genius',
                   'Using rock music to learn',
                   'https://img3.doubanio.com/view/photo/l/public/p2501863104.jpg',
                   'https://www.youtube.com/watch?v=3PsUJFEBC74')

# save movies into a list
movies = [toy_story, avatar, pirates_caribbean, bad_genius, school_of_rock, bad_genius]

# use fresh_tomatoes to open movie page
fresh_tomatoes.open_movies_page(movies)
