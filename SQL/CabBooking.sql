Create table cab_booking
(
	CabBookingId int auto_increment primary key,
    BookDate date,
    Location int,
    CurrentCap int,
    MaxCapacity int,
    IsBooked int,
    CabType varchar(20)
);
  alter table cab_booking
rename column CabBookingId to CabId;

alter table cab_booking
add column DriverName varchar(50);

alter table cab_booking
add column CarNo varchar(50);

alter table cab_booking
drop column BookDate;

desc cab_booking;
##Scenario 1: When I am booking a shared cab

#Step 1: Check if a waiting cab is present

Select * from cab_booking
where BookDate= '2022-04-26' and Location=421501 and CabType='shared' and IsBooked=0;

# Step 2.1 We do not get any output

Insert into Cab_Booking(BookDate, Location, CurrentCap, MaxCapacity, IsBooked, CabType)
Values ('2022-04-26', 421501, 1, 3, 0, 'shared');

# Step 2.2 Waiting already exists
Update cab_booking
set CurrentCap = CurrentCap +1,
IsBooked = If(CurrentCap=MaxCapacity,1,0)
where CabBookingId=2;
select * from cab_booking;
Update diya.cab_booking set CurrentCap=CurrentCap+1 where CabId=3

Update diya.cab_booking set CurrentCap=CurrentCap+1 where CabId=3

##Scenario 2: When I am booking a personal cab
Insert into Cab_Booking(BookDate, Location, CurrentCap, MaxCapacity, IsBooked, CabType)
Values ('2022-04-26', 421003, 1, 3, 1, 'personal');



### Scenario 3: When the employee is checking for status
Select * from cab_booking
where BookDate= '2022-04-26' and Location=421501 and CabType='shared'
order by CabBookingId desc limit 1;
Insert into Cab_Booking(BookDate, Location, CurrentCap, MaxCapacity, IsBooked, CabType)
Values ('2022-04-26', 400601, 1, 3, 0, 'shared');



Select * from cab_booking where BookDate= '2022-04-26' and Location=421501 and CabType='shared' order by CabBookingId desc limit 1;


#Employee details
Select employee.EmpFirstName,employee.EmpLastName,employee.EmpPincode from employee inner join user on employee.EmpFirstName=user.UserName;

#Booking Details
select * from employee inner join user on employee.EmpFirstName=user.UserName inner join cab_booking on employee.EmpPincode=cab_booking.Location