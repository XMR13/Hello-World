'''
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop
'''

#membuat fungsi yang mengembalikan dicitonary
def membuat_album(nama_musisi, nama_album, banyak_lagu = None):
    dictionary_album = {'Nama':nama_musisi, 'Album':nama_album}
    
    if banyak_lagu:
        dictionary_album['banyak lagu'] = banyak_lagu

    return dictionary_album

    
#membuat loopnya ygyg
while True:
    nama_musisi = input("Massukkan nama musisi! ")
    nama_album = input("Masukkan nama albumnya!")
    banyak_lagiu = input("masukkan banyak lagu(jika ada!!) ")
    hasil = membuat_album(nama_musisi,nama_album, banyak_lagu = banyak_lagiu)

    print(hasil,'\n')
    quitting = input('tekan q untuk keluar')
    if quitting =='q':
        break

