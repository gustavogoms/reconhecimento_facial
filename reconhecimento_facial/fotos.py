import face_recognition as fr
from engine import reconhece_face, get_rostos

desconhecido = reconhece_face("./img/gustavo.jpg")
if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nome_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    for i in range(len(nome_dos_rostos)):
        resultado = resultados[i]
        if(resultado):
            print("rosto do ", nome_dos_rostos[i], 'foi reconhecido')


else:
    print('Nao foi encontrado nenhum rosto')