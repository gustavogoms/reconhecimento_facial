import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos

    return False, []

def get_rostos():
    rostos_conhecidos = []
    nome_dos_rostos = []


    gustavo1 = reconhece_face("./img/gustavo1.jpg")
    if(gustavo1[0]):
        rostos_conhecidos.append(gustavo1[1][0])
        nome_dos_rostos.append("Gustavo")

    aurea = reconhece_face("./img/aurea.jpg")
    if(aurea[0]):
        rostos_conhecidos.append(aurea[1][0])
        nome_dos_rostos.append("aurea")

    return rostos_conhecidos, nome_dos_rostos