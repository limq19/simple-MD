import numpy as np

FILENAME = 'geo.in'
# Read the file
fread = open(FILENAME, 'r')
fCONTENTlist = [line.strip() for line in fread.readlines() if line.strip()]     # Read all the lines and Remove all blank lines
fCONTENT = np.array(fCONTENTlist)
fread.close()

a = np.char.find(fCONTENT, 'CELL_PARAMETER')
b = np.char.find(fCONTENT, 'ATOMIC_POSTION')
c = np.char.find(fCONTENT, 'ATOMIC_VELOCITY')
print(b)
print(type(a))
str_cell = fCONTENT[a + 1 : a + 3]
str_position = fCONTENT[b + 1 : c - 2]
str_velocity = fCONTENT[c + 1 :]
cell = np.array(np.char.split(str_cell).tolist())[:, 1:].astype(float)
position = np.array(np.char.split(str_position).tolist())[:, 1:].astype(float)
velocity = np.array(np.char.split(str_velocity).tolist())[:, 1:].astype(float)
print(cell)
print(position)
print(velocity)
# stringNORMALS = fCONTENT[np.char.find(fCONTENT, 'He')+1 > 0]
# coords = np.array(np.char.split(stringNORMALS).tolist())[:, 1:].astype(float)

# bohr = 1.8897161646321
# coords_bohr = coords * bohr
# coords_bohr_12 = np.round(coords_bohr, 12)

# # write the file
# fwrite = open('geo_bohr.in', 'w')
# fwrite.write('%ATOMIC_POSTION(BOHR)')
# for i in range(int(coords_bohr.size / 3)):
#     fwrite.write('\n' + str(i))
#     for j in range(3):
#         fwrite.write('   ' + '%.12g' % coords_bohr_12[i][j])
