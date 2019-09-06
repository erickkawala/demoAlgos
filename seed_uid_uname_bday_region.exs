alias Hello.Accounts.User
alias Hello.Repo
alias Hello

# 2019 - 1900 = 119 years;  119 / 4 (leap year) = 29.75
# so add 30 days to 364*119 = 43316 + 30 = 43346 days in loop
# 8365427 / 43346 = 192.99 matching sets of birth year/month/days

# for approx even num of birth_info and region distributions:
# 193 * 203 = 39179
# 39179*200 = 7835800 iterations for 200 set repetitions

# number of products: 143 indices: 0-142

# rand_group indices range from 0 to 10000
# trying some query stuff on this


# set n_stop in calling function to set iterations-1
#                n n_stop yrs mo days
# Insert.month_Jan(1,1000,1900, 1, 1)

defmodule Insert do

  @cities ["Whyalla","Rockingham","Prospect","Port Hedland","Perth","Murray Bridge","Mount Isa","Morphett Vale","Mandurah","Kwinana","Kalgoorlie","Gosnells","Geraldton","Gawler","Fremantle","Darwin","Busselton","Bunbury","Armadale","Alice Springs","Albany","Adelaide","Woodridge","Wodonga","Werribee","Warrnambool","Wantirna South","Wangaratta","Wagga Wagga","Traralgon","Townsville","Toowoomba","Thornbury","Thomastown","Tarneit","Taree","Tamworth","Sydney","Surfers Paradise","Sunnybank","Sunbury","Port Stephens","Springvale","Southport","South Grafton","Shepparton","Seaford","Saint Kilda","Saint Albans","Rowville","Rockhampton","Richmond","Reservoir","Queanbeyan","Quakers Hill","Preston","Port Macquarie","Point Cook","Pakenham South","Orange","Nowra","Northcote","Noble Park","Newcastle","Nerang","Narre Warren","Narangba","Mulgrave","Mount Martha","Mount Gambier","Mount Eliza","Mosman","Mornington","Morayfield","Moe","Mill Park","Mildura","Melton","Melbourne","Maryborough","Marrickville","Maroubra","Maitland","Mackay","Liverpool","Lismore","Lilydale","Launceston","Lara","Langwarrin","Lalor","Keysborough","Kew","Katoomba","Hornsby","Hobart","Hawthorn South","Hampton Park","Griffith","Greensborough","Granville","Goulburn","Gold Coast","Glenroy","Glenferrie","Gladstone","Geelong","Frankston East","Frankston","Forster","Essendon","Epping","Epping","Engadine","Eltham","Echuca","Earlwood","Dubbo","Doncaster East","Doncaster","Devonport","Deer Park","Deception Bay","Dandenong","Cronulla","Cranbourne","Cranbourne","Craigieburn","Coffs Harbour","Coburg","Clayton","Wollongong","Cessnock","Castle Hill","Carrum Downs","Carnegie","Carlingford","Caringbah","Canberra","Camberwell","Caloundra","Cairns","Caboolture","Burnie","Bundaberg","Buderim","Brunswick","Broken Hill","Brisbane","Boronia","Blacktown","Berwick","Bendigo","Baulkham Hills","Bathurst","Banora Point","Bankstown","Ballarat","Auburn","Ashfield","Armidale","Albury","South Brisbane","Cheltenham","Randwick","Dee Why","Umina","Palmerston","Bracken Ridge","North Ryde","Hoppers Crossing","Logan City","Carindale","Paramatta","Ferntree Gully","City of Parramatta","Adelaide Hills","Canning Vale","Glenmore Park","Glen Iris","Balwyn North","Carnegie","Malvern East","Brighton East","Booval","St Albans","Endeavour Hills","Clayton","Taylors Lakes","Roxburgh Park","Wyndham Vale","Willetton","Thornbury","Thornlie","Hillside","Bundoora","Forest Lake","Sunnybank Hills","Narre Warren South","Dandenong North","Frankston South","Sunshine West","Altona Meadows","West Pennant"]
  @subregions ["Aguascalientes","Baja California","Baja California Sur","Campeche","Chiapas","Chihuahua","Coahuila","Colima","Federal District","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco","Mexico","Morelos","Nayarit","Oaxaca","Puebla","Quintana Roo","Sinaloa","Sonora","Tabasco","Tamaulipas","Veracruz","Zacatecas","Avon","Bedfordshire","Berkshire","Borders","Bristol","Buckinghamshire","Cambridgeshire","Channel Islands","Cheshire","Cleveland","Cornwall","Cumbria","Derbyshire","Devon","Dorset","Durham","East Riding of Yorkshire","East Sussex","Essex","Gloucestershire","Greater Manchester","Hampshire","Herefordshire","Hertfordshire","Humberside","Isle of Man","Isle of Wight","Isles of Scilly","Kent","Lancashire","Leicestershire","Lincolnshire","London","Merseyside","Middlesex","Norfolk","North Yorkshire","Northamptonshire","Northumberland","Nottinghamshire","Oxfordshire","Rutland","Shropshire","Somerset","South Yorkshire","Chachapoyas","Bagua","Condorcanqui","Luya","Utcubamba","Huaraz","Aija","Antonio Raymondi","Bolognesi","Carhuaz","Carlos Fermín Fitzcarrald","Casma","Corongo","Huari","Huarmey","Huaylas","Mariscal Luzuriaga","Ocros","Pallasca","Pomabamba","Recuay","Yungay","Abancay","Antabamba","Aymaraes","Cotabambas","Chincheros","Grau","Arequipa","Castilla","Caylloma","Condesuyos","Islay","Huamanga","Cangallo","Huanta","La Mar","Lucanas","Parinacochas","Sucre","Cajamarca","Cajabamba","Chota","Cutervo","San Ignacio","San Marcos","San Miguel","San Pablo","Santa Cruz","Callao","Cusco","Acomayo","Anta","Calca","Canas","Canchis","Chumbivilcas","Espinar","Paruro","Paucartambo","Quispicanchi","Urubamba","Huancavelica","Acobamba","Angaraes","Castrovirreyna","Churcampa","Tayacaja","Ambo","Dos de Mayo","Huacaybamba","Leoncio Prado","Pachitea","Puerto Inca","Lauricocha","Yarowilca","Ica","Chincha","Nazca","Palpa","Pisco","Huancayo","Chanchamayo","Jauja","Satipo","Tarma","Yauli","Chupaca","Trujillo","Ascope","Otuzco","Lima","Huaura","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Maine","Maryland","Massachusetts","Michigan","Minnesota","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","South Dakota","Texas","Utah","Vermont","Virginia","Washington","Wisconsin","Wyoming"]
  @countries ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua & Deps","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Rep","Chad","Chile","China","Colombia","Comoros","Congo","Congo {Democratic Rep}","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland {Republic}","Israel","Italy","Ivory Coast","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea North","Korea South","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar, {Burma}","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russian Federation","Rwanda","St Kitts & Nevis","St Lucia","Saint Vincent & the Grenadines","Samoa","San Marino","Sao Tome & Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican country","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe","Afghanistan","Albania","Algeria","Andorra","Angola","Antigua & Deps","Argentina","Armenia"]
          
  def month_Jan(n, n_stop, years, months, days) do

    if n == n_stop do
      exit(:shutdown)
    end

    index_to_insert = rem(n,203)

    country = Enum.at(@countries, index_to_insert)
    subregion = Enum.at(@subregions, index_to_insert)
    city = Enum.at(@cities, index_to_insert)

    group = rem(n,1000)
    
    Hello.Repo.insert!(%Hello.Accounts.User
    {
      id: n,
      name: "User#{n}",
      username: "Username#{n}",
      birth_year: years,
      birth_month: months,
      birth_day: days,
      country: "#{country}",
      subregion: "#{subregion}",
      city: "#{city}",
      group: "#{group}"
    })

    if days == 31 do
      if rem(years,4) == 0 do
        month_Feb_leap(n+1, n_stop, years, months+1, 1)
      else
        month_Feb(n+1, n_stop, years, months+1, 1)
      end
    end

    #recurse for 31 days ^^
    month_Jan(n+1, n_stop, years, months, days+1)
  end


  def month_Feb(n, n_stop, years, months, days) do

    if n == n_stop do
      exit(:shutdown)
    end

    index_to_insert = rem(n,203)

    country = Enum.at(@countries, index_to_insert)
    subregion = Enum.at(@subregions, index_to_insert)
    city = Enum.at(@cities, index_to_insert)

    group = rem(n,1000)
        
    Hello.Repo.insert!(%Hello.Accounts.User
    {
      id: n,
      name: "User#{n}",
      username: "Username#{n}",
      birth_year: years,
      birth_month: months,
      birth_day: days,
      country: "#{country}",
      subregion: "#{subregion}",
      city: "#{city}",
      group: "#{group}"
    })

    if days == 28 do 
      months_31(n+1, n_stop, years, months+1, 1)
    end

    month_Feb(n+1, n_stop, years, months, days+1)
  end


  def months_30(n, n_stop, years, months, days) do

    if n == n_stop do
      exit(:shutdown)
    end

    index_to_insert = rem(n,203)

    country = Enum.at(@countries, index_to_insert)
    subregion = Enum.at(@subregions, index_to_insert)
    city = Enum.at(@cities, index_to_insert)

    group = rem(n,1000)
        
    Hello.Repo.insert!(%Hello.Accounts.User
    {
      id: n,
      name: "User#{n}",
      username: "Username#{n}",
      birth_year: years,
      birth_month: months,
      birth_day: days,
      country: "#{country}",
      subregion: "#{subregion}",
      city: "#{city}",
      group: "#{group}"
    })

    if days == 30 do
      months_31(n+1, n_stop, years, months+1, 1)
    end

    months_30(n+1, n_stop, years, months, days+1)
  end


  def months_31(n, n_stop, years, months, days) do

    if n == n_stop do
      exit(:shutdown)
    end

    index_to_insert = rem(n,203)

    country = Enum.at(@countries, index_to_insert)
    subregion = Enum.at(@subregions, index_to_insert)
    city = Enum.at(@cities, index_to_insert)

    group = rem(n,1000)
        
    Hello.Repo.insert!(%Hello.Accounts.User
    {
      id: n,
      name: "User#{n}",
      username: "Username#{n}",
      birth_year: years,
      birth_month: months,
      birth_day: days,
      country: "#{country}",
      subregion: "#{subregion}",
      city: "#{city}",
      group: "#{group}"
    })

    if months == 12 and days == 31 and years == 2019 do
      month_Jan(n+1, n_stop, 1900,  1,   1)
    end

    if months == 7 and days == 31 do
      month_Aug(n+1, n_stop, years, months+1, 1)
    end
    if rem(n,365) == 0 do
      month_Jan(n+1, n_stop, years+1,  1,   1)
    end

    if days == 31 do
      months_30(n+1, n_stop, years, months+1, 1)
    end

    months_31(n+1, n_stop, years, months, days+1)
  end


  def month_Aug(n, n_stop, years, months, days) do

    if n == n_stop do
      exit(:shutdown)
    end

    index_to_insert = rem(n,203)

    country = Enum.at(@countries, index_to_insert)
    subregion = Enum.at(@subregions, index_to_insert)
    city = Enum.at(@cities, index_to_insert)

    group = rem(n,1000)
    
    Hello.Repo.insert!(%Hello.Accounts.User
    {
      id: n,
      name: "User#{n}",
      username: "Username#{n}",
      birth_year: years,
      birth_month: months,
      birth_day: days,
      country: "#{country}",
      subregion: "#{subregion}",
      city: "#{city}",
      group: "#{group}"
    })

    if days == 31 do
      months_30(n+1, n_stop, years, months+1, 1)
    end

    month_Aug(n+1, n_stop, years, months, days+1)
  end


  def month_Feb_leap(n, n_stop, years, months, days) do

    index_to_insert = rem(n,203)

    country = Enum.at(@countries, index_to_insert)
    subregion = Enum.at(@subregions, index_to_insert)
    city = Enum.at(@cities, index_to_insert)

    group = rem(n,1000)
    
    Hello.Repo.insert!(%Hello.Accounts.User
    {
      id: n,
      name: "User#{n}",
      username: "Username#{n}",
      birth_year: years,
      birth_month: months,
      birth_day: days,
      country: "#{country}",
      subregion: "#{subregion}",
      city: "#{city}",
      group: "#{group}"
    })

    if days == 29 do 
      months_31(n+1, n_stop, years, months+1, 1)
    end

    month_Feb_leap(n+1, n_stop, years, months, days+1)
  end
end

#call entire loop, 
#                n n_stop yrs mo days
# 
Insert.month_Jan(1,7835801,1900, 1, 1)

