'''
for i in range(12):
    print("##################################################")
    print("if self.conf.has_section(\"42" + str(i) + "\") == True:")
    print("    self.m_comboBox42" + str(i) + ".SetValue(self.conf.get(\"42" + str(i) + "\", \"value\"))")     
    print("else:")
    print("    self.conf.add_section(\"42" + str(i) + "\")")
    print("    self.conf.set(\"42" + str(i) + "\", \"value\", \"大\")")
    print("#")
    print("if self.conf.has_section(\"43" + str(i) + "\") == True:")
    print("    self.m_textCtrl43" + str(i) + ".SetValue(self.conf.get(\"43" + str(i) + "\", \"value\"))")     
    print("else:")
    print("    self.conf.add_section(\"43" + str(i) + "\")")
    print("    self.conf.set(\"43" + str(i) + "\", \"value\", \"10\") ")              
    print("#")
    print("if self.conf.has_section(\"44" + str(i) + "\") == True:")
    print("    self.m_textCtrl44" + str(i) + ".SetValue(self.conf.get(\"44" + str(i) + "\", \"value\"))")    
    print("else:")
    print("    self.conf.add_section(\"44" + str(i) + "\")")
    print("    self.conf.set(\"44" + str(i) + "\", \"value\", \"1" + str(i) + "\") ")         
    print("#")
    print("if self.conf.has_section(\"45" + str(i) + "\") == True:")
    print("    self.m_textCtrl45" + str(i) + ".SetValue(self.conf.get(\"45" + str(i) + "\", \"value\"))")     
    print("else:")
    print("    self.conf.add_section(\"45" + str(i) + "\")")
    print("    self.conf.set(\"45" + str(i) + "\", \"value\", \"10\")")                
    print("#")
    print("if self.conf.has_section(\"46" + str(i) + "\") == True:")
    print("    self.m_checkBox46" + str(i) + ".SetValue(isTrue(self.conf.get(\"46" + str(i) + "\", \"value\")))")   
    print("else:")
    print("    self.conf.add_section(\"46" + str(i) + "\")")
    print("    self.conf.set(\"46" + str(i) + "\", \"value\", \"True\")")  
    print("##################################################")
'''
'''
for i in range(12):    
    print("##################################################")
    print("self.conf.set(\"42" + str(i) + "\", \"value\", self.m_comboBox42" + str(i) + ".GetValue())")
    print("self.conf.set(\"43" + str(i) + "\", \"value\", self.m_textCtrl43" + str(i) + ".GetValue())")
    print("self.conf.set(\"44" + str(i) + "\", \"value\", self.m_textCtrl44" + str(i) + ".GetValue())") 
    print("self.conf.set(\"45" + str(i) + "\", \"value\", self.m_textCtrl45" + str(i) + ".GetValue())")
    print("self.conf.set(\"46" + str(i) + "\", \"value\", bool2str(self.m_checkBox46" + str(i) + ".GetValue()))")
    ##################################################
'''
for i in range(12): 	
	print("##################################################")
	print("target[\"42" + str(i) + "\"] = self.m_comboBox42" + str(i) + ".GetValue()")
	print("target[\"43" + str(i) + "\"] = self.m_textCtrl43" + str(i) + ".GetValue()")
	print("target[\"44" + str(i) + "\"] = self.m_textCtrl44" + str(i) + ".GetValue()")
	print("target[\"45" + str(i) + "\"] = self.m_textCtrl45" + str(i) + ".GetValue()")
	print("target[\"46" + str(i) + "\"] = self.m_checkBox46" + str(i) + ".GetValue()")
