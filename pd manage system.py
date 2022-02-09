class PdDepartment():

	def __init__(self):
		self.pd_manager_list=[]
		self.program_list=[]
		self.design_company_list=[]
		self.major_designer_dict={}

	def add_pd_manager(self,pd_manager_obj):
		self.pd_manager_list.append(pd_manager_obj)
		print(f"新员工{pd_manager_obj.name}加入设计部")
	
	def add_program(self,program_obj,pd_manager_obj,design_company_obj):
		self.program_list.append(program_obj)
		print(f"项目{program_obj.name}由产品策划部{pd_manager_obj.name}负责，由设计公司{design_company_obj.name}设计")
	
	def add_design_company(self,design_company_obj):
		self.design_company_list.append(design_company_obj)
		print(f"设计单位{design_company_obj.name}入库")

	def add_major_designer(self,design_company_obj):
		self.major_designer_dict[design_company_obj.name]= design_company_obj.major_designer_list
		print(f"{design_company_obj.name}的主要设计师{design_company_obj.major_designer_list}已经入库")


class PdManager():

	def __init__(self,name,age,major,pd_department_obj):
		self.name= name
		self.age= age
		self.major= major
		self.program_list=[]#项目列表
		self.dwg_list=[]#图纸列表
		self.changer_list=[]#变更列表
		self.metarial_list=[]#材料样品列表
		self.info_designer_list=[]
		pd_department_obj.add_pd_manager(self)

	def add_program(self,program_obj):
		self.program_list.append(program_obj)
		print(f"{self.name}进入了项目{program_obj.name}团队")

	def info_designer(self,program_obj,major_designer_obj,info):
		print(f"甲方设计{self.name}向{major_designer_obj.name}负责的{program_obj.name}项目，发出了{info}需求")
		major_designer_obj.accept_info(self,info)

	def check(self,major_designer_obj,files_obj):
		if files_obj.kind == "dwg":
			major_designer_obj.post(self,files_obj)
			print(f"甲方设计{self.name}审核{files_obj.name}完成")
			self.dwg_list.append(files_obj)
		elif files_obj.kind == "changer":
			major_designer_obj.post(self,files_obj)
			print(f"甲方设计{self.name}审核{files_obj.name}完成")
			self.changer_list.append(files_obj)
		elif files_obj.kind == "metarial":
			major_designer_obj.post(self,files_obj)
			print(f"甲方设计{self.name}审核{files_obj.name}完成")
			self.metarial_list.append(files_obj)
		
	def post(self,files_obj,program_manager_obj):
		if files_obj in (self.dwg_list or self.changer_list or self.metarial_list):
			print(f"甲方设计{self.name}下发{files_obj.name}")
			program_manager_obj.accept_files(self,files_obj)


class DesignCompany():
	def __init__(self,name):
		self.name = name 
		self.major_designer_list=[]
		self.program_list=[]
	def add_major_designer(self,major_designer_obj):
		self.major_designer_list.append(major_designer_obj)
		print(f"设计师{major_designer_obj.name}加入{self.name}设计公司")
	def add_program(self,program_obj):
		self.program_list.append(program_obj)
		print(f"{program_obj.name}项目已经委托由{self.name}设计公司进行设计")


class MajorDesigner():
	def __init__(self,name,age,major,design_company_obj):
		self.name= name
		self.age= age
		self.major= major
		self.program_list=[]
		design_company_obj.add_major_designer(self)
	
	def accept_info(self,pd_manager_obj,info):
		print(f"设计师{self.name}接收到了来自甲方{pd_manager_obj.name}的{info}需求")

	def post(self,pd_manager_obj,files_obj):
		print(f"设计师{self.name}上传{files_obj.name}给甲方{pd_manager_obj.name}")


class ProgramDepartment():

	def __init__(self,name):
		self.name = name 
		self.program_list=[]
		self.construction_company_list=[]
		self.major_worker_dict={}
		self.program_manager_list=[]

	def add_program(self,program_obj,program_manager_obj,construction_company_obj):
		self.program_list.append(program_obj)
		print(f"{program_obj.name}项目由工程管理部{program_manager_obj.name}负责，由建设单位{construction_company_obj.name}建设")

	def add_construction_company(self,construction_company_obj):
		self.construction_company_list.append(construction_company_obj)
		print(f"建设单位{construction_company_obj.name}加入{self.name}项目部")

	def add_major_worker(self,construction_company_obj):
		self.major_worker_dict[construction_company_obj.name]=construction_company_obj.major_worker_list
		print(f"{construction_company_obj.name}的施工经理{construction_company_obj.major_worker_list}")

	def add_program_manager(self,program_manager_obj):
		self.program_manager_list.append(program_manager_obj)
		print("【----------员工入职通知----------】")
		print(f"新员工{program_manager_obj.name}加入项目部")


class ProgramManager():
	
	def __init__(self,name,age,major,program_department_obj):
		self.name = name
		self.age = age
		self.major = major
		self.program_list=[]#项目列表
		program_department_obj.add_program_manager(self)

	def accept_files(self,pd_manager_obj,files_obj):
		print(f"{self.name}接收到来自设计端口{pd_manager_obj.name}的{files_obj.name}文件")

	def add_program(self,program_obj):
		self.program_list.append(program_obj)
		print(f"{self.name}进入了项目{program_obj.name}团队")


class ConstructionCompany():
	
	def __init__(self,name,major_worker):
		self.name = name 
		self.major_worker_list= [major_worker]
		self.program_list=[]

	def add_program(self,program_obj):
		self.program_list.append(program_obj)
		print(f"{program_obj.name}项目已经委托由{self.name}公司进行建设")


class Program():

	def __init__(self,name,address,area,kind,level,stage):
		self.name = name
		self.address= address
		self.area= area
		self.kind= kind
		self.level= level
		self.stage= stage
		self.team_staff=[]
		print(f"新项目{self.name}获取，面积{self.area},产品类型为{self.kind},属于{self.level}档项目")
	
	def creat_program_team(self,pd_manager_obj,program_manager_obj,pd_department_obj,program_department_obj,design_company_obj,construction_company_obj):
		self.team_staff.append(pd_manager_obj)
		self.team_staff.append(program_manager_obj)
		self.team_staff.append(pd_department_obj)
		self.team_staff.append(program_department_obj)
		self.team_staff.append(design_company_obj)
		self.team_staff.append(construction_company_obj)
		program_department_obj.add_program(self,program_manager_obj,construction_company_obj)
		pd_department_obj.add_program(self,pd_manager_obj,design_company_obj)
		pd_manager_obj.add_program(self)
		program_manager_obj.add_program(self)
		design_company_obj.add_program(self)
		construction_company_obj.add_program(self)


class FilesObj():
	def __init__(self,name,kind):
		self.name = name 
		self.kind = kind


pd_department1= PdDepartment()
pd_manager1= PdManager("大白",29,"Arch",pd_department1)
design_company1= DesignCompany("AAD")
major_designer1= MajorDesigner("小黑",24,"Arch",design_company1)
program_department1 = ProgramDepartment("毛庄项目部")
program_manager1= ProgramManager("大黑",32,"Engineer",program_department1)
construction_company1= ConstructionCompany("万华","大灰")
program1 = Program("毛庄","毛庄路",120000,"高层住宅","TOP","方案阶段")
files_obj1= FilesObj("地下车库图纸","dwg")

program1.creat_program_team(pd_manager1,program_manager1,pd_department1,program_department1,design_company1,construction_company1)

pd_manager1.check(major_designer1,files_obj1)
pd_manager1.post(files_obj1,program_manager1)