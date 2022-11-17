create table Employee
(
    EmpId int PRIMARY key,
	EmpFirstName varchar(200),
	EmpLastName varchar(200),

    EmpBranch varchar(500),
    EmpStreet varchar(200),
    EmpCity varchar(200),
    EmpPincode varchar(200),
    EmpContactNo varchar(200),
    EmpEmail varchar(200)
);

Insert into Employee(EmpId,EmpFirstName,EmpLastName,EmpBranch,EmpStreet,EmpCity,EmpPincode,EmpContactNo,EmpEmail)
Values(1, 'Hazel','Grey','Software Developer','Jai Hind','Unr','421002','9876543210','hazel@aces.ac.in');