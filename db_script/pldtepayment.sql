create table bankAccount (
	accountno int primary key,
	balance decimal(9,2)
);

create or replace
    function set_bankaccount(p_accountno int,  p_balance decimal(9,2)) 
    returns text as 
$$
    begin
      insert into bankAccount(accountno, balance) values
        (p_accountno, p_balance);
    return 'OK';
    end;
$$
  language  'plpgsql';


create or replace function
     get_balance(in int, out decimal(9,2))
     returns decimal(9,2) as
$$
     select balance from bankAccount
     where accountno = $1;   
$$
  language  'sql';
  
 -- end of bankaccount table
 
 -- start of pldtaccount table
 create table pldtAccount (
	pldtacct int primary key,
	bill decimal(9,2)
);

create or replace
    function set_pldtaccount(p_pldtacct int,  p_bill decimal(9,2)) 
    returns text as 
$$
    begin
      insert into pldtAccount(pldtacct, bill) values
        (p_pldtacct, p_bill);
    return 'OK';
    end;
$$
  language  'plpgsql';


create or replace function
     get_bill(in int, out decimal(9,2))
     returns decimal(9,2) as
$$
     select bill from pldtAccount
     where pldtacct = $1;   
$$
  language  'sql';
  
 -- end of pldtaccount table
 
 -- start of paybill table
 create table payBill (
	receiptNo serial NOT NULL primary key,
	accountno int references bankAccount(accountno),
	pldtacct int references pldtAccount(pldtacct)
);

create or replace
    function set_payment(p_accountno int,  p_pldtacct int) 
    returns text as 
$$
	declare
	receipt int;
    begin
      insert into payBill(accountno, pldtacct) values
        (p_accountno, p_pldtacct);
    return receipt;
    end;
$$
  language  'plpgsql';

-- end of paybill table

-- start of receipt table
create table receipt (
	receipt_pk serial NOT NULL primary key,
	receiptNo int references payBill(receiptNo),
	timedate timestamp,
	amount decimal(9,2) references pldtAccount(bill)
);

create or replace
    function set_receipt(p_receiptNo int,  p_timedate timestamp, p_amount decimal(9,2)) 
    returns text as 
$$
    begin
      insert into receipt(receiptNo, timedate, amount) values
        (p_receiptNo, p_timedate, p_amount);
    return 'OK';
    end;
$$
  language  'plpgsql';


create or replace function
     get_receipt(in int, out int, out timestamp, out decimal(9,2))
     returns setof record as
$$
     select receiptNo, timedate, amount from receipt
     where receipt_pk = $1;   
$$
  language  'sql';