import media
import fresh_tomatoes

""" This file triggers the web creation,
    imports media where our model is stored
    and fresh_tomatoes that generates the webpage
    in this case we're generating a seasonal anime website
"""

arslan_senki = media.Anime(
    "Arslan Senki",
    "At the age of 14, Arslan goes to his first battle and loses everything as\
    the blood-soaked mist of war gives way to scorching flames, bringing him to\
    face the demise of his once glorious kingdom. However, it is Arslan's\
    destiny to be a ruler, and despite the trials that face him, he must now\
    embark on a journey to reclaim his fallen kingdom.",
    "http://anilist.co/img/dir/anime/reg/20935-nMV41twhNq93.jpg",
    "https://youtu.be/CWL5pcfEyKk")

fate_stay = media.Anime(
    "Fate/stay night: ULW",
    "The 2nd season of ufotable's adaptation of the Unlimited Blade Works route\
    of Fate/stay night.",
    "http://anilist.co/img/dir/anime/reg/20792-463frI6M1L7K.jpg",
    "https://youtu.be/1X8ZBVgairo")

grisaia_no_rakuen = media.Anime(
    "Grisaia no Rakuen",
    "The Grisaia no Rakuen visual novel continues the Grisaia no Meikyuu visual\
    novel's main route and concludes the trilogy. It also includes a prologue\
    following the five heroines as they arrive at Mihama Academy.",
    "http://anilist.co/img/dir/anime/reg/21006-QHBk1CrhRi2w.png",
    "https://youtu.be/cXI6Rb3RqSg")

nisekoi_2 = media.Anime(
    "Nisekoi:",
    "Season 2 of Nisekoi",
    "http://anilist.co/img/dir/anime/reg/20876-eIgUEmjn97Nf.jpg",
    "https://youtu.be/_Yks4CKOUOA")

yamada_kun = media.Anime(
    "Yamadakun to Nananin no Majo",
    "Ryu Yamada is a second year student at Suzaku High. Ryu is always late for\
    school, naps in class and gets abysmal grades. His life is a dead bore. The\
    beautiful Urara Shiraishi, on the other hand, is Suzaku High's brightest\
    student. One day, without explanation, their bodies are swapped! Ryu ends\
    up in Urara's body, and Urara in Ryu's.",
    "http://anilist.co/img/dir/anime/reg/20966-TYRotSnAtx5q.jpg",
    "https://youtu.be/vDOknfJIUu4")

sidonia_2 = media.Anime(
    "Sidonia no Kishi: Daikyuu Wakusei Seneki",
    "Having narrowly avoided the collision with the asteroid, the Sidonia sets\
    a course for the Lem system in order to wipe out the Gauna nest.",
    "http://anilist.co/img/dir/anime/reg/20762-LQxZiA3X405M.jpg",
    "https://youtu.be/DiZJkYg4n1E")

movies = [arslan_senki, fate_stay, grisaia_no_rakuen,
          nisekoi_2, yamada_kun, sidonia_2]

fresh_tomatoes.open_movies_page(movies)
