cells = ({'cell_1':[31,201,64,219],'cell_2':[63,201,110,219],'cell_3':[111,202,159,220],'cell_4':[157,202,305,221],'cell_5':[304,203,359,221],'cell_6':[356,203,393,221],'cell_7':[390,203,456,222],'cell_8':[456,204,528,222],'cell_9':[527,205,590,222],'new_row1':[30,249,67,260],'new_row2':[66,251,307,256],'new_row3':[306,246,359,257],'new_row4':[359,242,402,255],'new_row5':[402,242,453,257],'new_row6':[453,245,530,257],'new_row7':[530,243,599,630]})

cell_center=dict()
cell_last = dict()
#getting centers of each cell
for element in cells:
	cell_center[element] = cells.get(element)[:2]
	cell_last[element] = cells.get(element)[2:]
	
cell_first = cell_center


#getting first cell
l = [sum(i) for i in cell_center.values()]
first_cell = list(cell_center.keys())[l.index(min(l))]
first_cell_value = cell_center.get(first_cell)
#optional : sort the dictionary according to items and get the first element as first cell

cells_done=[]
#cells_done.append(first_cell)
#to get next cell horizontally adjacent
def get_adjacent_cell(cell_center,first_cell, threshold):
    if first_cell not in cells_done: 
        for i in cell_center.keys():
            current_centers = cell_center.get(i)
            first_cell_value = cell_center.get(first_cell)
            if first_cell_value[0] < current_centers[0] and first_cell_value[1]-threshold <= current_centers[1]<=first_cell_value[1]+threshold:
                cells_done.append(first_cell)
                return i
                break
 
 #break because we only need one next cell
''' 
cell_center = {k: v for k, v in sorted(cell_center.items(), key=lambda item: item[1])}  
next_cell = get_adjacent_cell(cell_center,first_cell,threshold=1)
print(next_cell)


first_cell_value =  (259.0, 293.0)
next_cell = get_adjacent_cell(cell_center,first_cell,threshold=1)

#to get result for cells which are adjacent vertically --> reverse the if condition of get_adjacent_cell()

'''


cell_center = {k: v for k, v in sorted(cell_center.items(), key=lambda item: sum(item[1]))} 




relation = dict()
for i in cell_center:
    
    next_cell = get_adjacent_cell(cell_center,i,threshold=10)
    relation[i] = next_cell

r = 0
c = -1
new_row = 0
first_cell = list(relation.keys())[0]
row_columns_count = dict()
first = [first_cell]


def min_distance(first_cell,dictionary,index):
    d = [abs(first_cell[index] - x[index]) for x in list(dictionary.values())]    
    return list(dictionary.keys())[d.index(min(d))]
        
#print(relation)  
total_columns=0       
for i in range(len(relation)):
	if first_cell != None:
		c+=1
		r=r
		row_columns_count[first_cell] = (r,c)
		current_cell = first_cell
		first_cell = relation[first_cell]
		if current_cell not in first: 
		    del cell_center[current_cell]

	else:  
		new_row+=1
		if new_row==1:
			total_column = c+1
		c = 0
		r = new_row
		nearest  = cell_center[first[-1]]
		del cell_center[first[-1]]
		first_cell = min_distance(nearest, cell_center,index=0)
		row_columns_count[first_cell] = (r,c)
		current_cell = first_cell
		first.append(first_cell)
		first_cell = relation[first_cell]


print(total_column)

for i in row_columns_count:
   print('{}  ==>  {}'.format(i,row_columns_count.get(i)))
'''
def get_area(x1,y1,x2,y2):
	area = (x2-x1)*(y2-y1)
	return area

		
def check_span(cell_id):
	(x1,y1) = cell_first[cell_id]
	(x2,y2) = cell_last[cell_id]
	current_area = get_area(x1,y1,x2,y2)
	areas = []
	upper_cell_index = list(row_columns_count.keys()).index(cell_id) % total_column	
	upper_cell_value = list(cell_first.keys())[upper_cell_index]
	
	(x1,y1) = cell_first[upper_cell_value]
	(x2,y2) = cell_last[upper_cell_value]
	first_area = get_area(x1,y1,x2,y2)
	areas.append(first_area)
	
	for i in range(total_column-upper_cell_index-1):
		print(upper_cell_value)
		(x2,y2) = cell_last[relation[upper_cell_value]]
		area_rectangle = get_area(x1,y1,x2,y2)
		upper_cell_value = relation[upper_cell_value]
		areas.append(area_rectangle)

	if areas == []:
		result = 1
	else:
		compute = [abs(x - current_area) for x in areas]
		
		minimum_difference = min(compute)
		result = compute.index(minimum_difference)+1
	print('{} -- {} -- {} -- {} -- {} -- {}'.format(cell_id,upper_cell_index,upper_cell_value,areas,result,current_area))
	return result
	

all_span = []
for i , j in enumerate(row_columns_count.keys()):
	
	if i < total_column:
		all_span.append(1)
	else:
		span = check_span(j)
		
		all_span.append(span)
		
'''


'''
import cv2
img = cv2.imread('C:/Users/rajes/Desktop/dhruv/file4.jpg')
for element in list(row_columns_count.keys()):  
    coordinates = cells[element]
    cv2.rectangle(img,(coordinates[0],coordinates[1],coordinates[2],coordinates[3]),(0,0,255),1)
    cv2.putText(img,str(row_columns_count[element]),(coordinates[0],coordinates[1]-2),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,cv2.LINE_AA,False)
    
cv2.imwrite('output.jpg',img)
'''
    
