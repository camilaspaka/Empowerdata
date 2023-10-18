#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Semana do Python na Pratica")


# In[2]:


print("Minha primeira vez usando o Jupyter!")


# In[3]:


print("10")


# In[4]:


type("10")


# In[5]:


print(10.5)


# In[6]:


type(10.5)


# In[7]:


print(10+1)


# In[8]:


print(10-5)


# In[9]:


print(10*10)


# In[10]:


print(100/10)


# In[11]:


print("10+20")


# In[12]:


print("10"+10)


# In[ ]:


input()


# In[ ]:


input("Digite o seu nome: ")
input("Digite a sua idade: ")


# In[ ]:





# In[ ]:


nome = "Semana do Python"
print(nome)


# In[ ]:


numero1=10
numero2=20
resultado=numero1+numero2
print(resultado)


# In[ ]:


type(nome)


# In[ ]:


type(idade)


# In[ ]:


print(int(idade)+10)


# In[ ]:


print(float(peso)+10)


# In[ ]:


type(10)


# In[ ]:


type(str(10))


# In[ ]:


nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")


# In[ ]:


print(f"Meu nome é {nome} e eu tenho {idade} anos!!!")


# In[ ]:


projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estimado = input("Digite o prazo estimado: ")


# In[ ]:


valor_total_estimado = int(horas_estimadas) * int(valor_hora)


# In[ ]:


print(valor_total_estimado)


# In[ ]:


get_ipython().system('pip install fpdf')


# In[ ]:


from fpdf import FPDF


# In[ ]:


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")


# In[ ]:


pdf.image("template.png", x=0, y=0 )

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_estimado))


# In[ ]:


pdf.output("orçamento.pdf")
print("O orçamento foi gerado com sucesso!!!")


# In[ ]:




