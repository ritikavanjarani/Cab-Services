create table cab
(
CabId int auto_increment primary key,
DriverName varchar(200),
DriverContact bigint,
CarNumber varchar(20),
CarModel varchar(50),
Capacity int
);

insert into cab(DriverName, DriverContact, CarNumber, CarModel, Capacity)
values('Bob',9898989898,'MH-004','Hyundai i10',3);

insert into cab(DriverName, DriverContact, CarNumber, CarModel, Capacity)
values('Steve',9090909090,'MH-002','Suzuki Desire',3);

insert into cab(DriverName, DriverContact, CarNumber, CarModel, Capacity)
values('Joey',8686868686,'MH-005','Baleno',3);

insert into cab(DriverName, DriverContact, CarNumber, CarModel, Capacity)
values('Chandler',9090909090,'MH-001','Verna',3);

select * from cabadmin