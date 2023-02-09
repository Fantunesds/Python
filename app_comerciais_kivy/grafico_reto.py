from matplotlib import pyplot as plt

plt.plot([1,2,3], [4,5,6], '-', color='#ebde34', lw=2)
#plt.title('Usando Python')
plt.title('Título esquerda',fontdict={'family':'serif','color':'darkblue','weight':'bold','size':16},loc='left')
plt.title('Título central',fontdict={'family':'monospace','color':'red','weight':'bold','size':16},loc='center')
plt.title('Título direita',fontdict={'family':'fantasy','color':'black','weight':'bold','size':16},loc='right')
plt.show()