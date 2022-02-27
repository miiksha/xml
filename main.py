<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<!-- 20-К-АС2 ПЕРВАЯ ЯЧЕЙКА -->

<!DOCTYPE AddressBook [
<!ELEMENT AddressBook (Human*)>
<!ELEMENT Human (FirstName,LastName,Patronymic,City,ListWorkplace,ListMobilePhone,ListHomePhone,Picture)>
<!ELEMENT FirstName (#PCDATA)>
<!ELEMENT LastName (#PCDATA)>
<!ELEMENT Patronymic (#PCDATA)>
<!ELEMENT City (#PCDATA)>
<!ELEMENT ListWorkplace (Workplace*)>
<!ELEMENT Workplace (#PCDATA|Position)*>
<!ELEMENT Position (#PCDATA)>
<!ELEMENT ListMobilePhone (Number*)>
<!ELEMENT Number (#PCDATA)>
<!ELEMENT ListHomePhone (Number*)>
<!ELEMENT Picture (#PCDATA)>
<!ATTLIST Picture href CDATA #IMPLIED>
]>


<AddressBook>

  <Human>
    <FirstName>Артём</FirstName>
    <LastName>Головатов</LastName>
    <Patronymic>Александрович</Patronymic>
    <City>Краснодар</City>
    <ListWorkplace>
      <Workplace>ООО Пятерочка
        <Position>Кассир</Position>
        <Position>Сборщик</Position>
      </Workplace>
      <Workplace>ООО Магнит
        <Position>Менеджер</Position>
        <Position>Тестировщик</Position>
      </Workplace>
    </ListWorkplace>
    <ListMobilePhone>
      <Number>89282418888</Number>
      <Number>89282412418</Number>
    </ListMobilePhone>
    <ListHomePhone>
      <Number>2535388</Number>
    </ListHomePhone>
    <Picture href="/People/AGolovatov.jpg"/>

  </Human>

</AddressBook>
