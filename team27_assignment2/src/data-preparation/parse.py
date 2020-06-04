import json

f = open('../../gen/data-preparation/temp/Fortniteastronomicalevent.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('Screenname\tcreated_at\tlocation\ttext\n')

cnt = 0
for line in con:
    
    cnt+=1
    obj = json.loads(line.replace('\n',''))
    
    location = str(obj.get('user').get('location'))

    USA = ['Atlanta','Atlanta, GA','Austin','Austin, TX','Baltimore','Boston','Boston, MA','Brooklyn','California','California, USA','Camden','Catoosa','Chicago','Cleveland','Columbus','Dallas','Danville','Florida','Florida, USA','Hollywood','Houston','Houston, TX',
           'Illinois','Indiana','Kentucky','Las Vegas','Los Angeles','Los Angeles, CA', 'Las Vegas, NV','Louisville','Manhattan',
           'Maryland','Maryland, USA','Marysville','Miami','Miami, FL','New Jersey','New York','New York, NY','New York, USA','North Carolina',
           'North America','NYC','Oakland','Orlando','Orlando, FL','Philadelphia','Queens','San Diego','San Diego, CA','San Fransisco, CA','San Fransisco',
           'South Carolina','South Carolina, USA','South Dakota','Tampa','Texas','Texas, USA','U.S.','United States','USA','Utah',
           'Virginia','Wisconsin','Wellington']
    
    if (str(location) in USA): location = 'USA'
    
    if (0==1):
        if (str(location)=='Atlanta'): location = 'USA'
        if (str(location)=='Atlanta, GA'): location = 'USA'
        if (str(location)=='Austin'): location = 'USA'
        if (str(location)=='Austin, TX'): location = 'USA'
        if (str(location)=='Baltimore'): location = 'USA'
        if (str(location)=='Boston'): location = 'USA'
        if (str(location)=='Boston, MA'): location = 'USA'
        if (str(location)=='Brooklyn'): location = 'USA'
        if (str(location)=='California'): location = 'USA'
        if (str(location)=='California, USA'): location = 'USA'
        if (str(location)=='Camden'): location = 'USA'
        if (str(location)=='Catoosa'): location = 'USA'
        if (str(location)=='Chicago'): location = 'USA'
        if (str(location)=='Cleveland'): location = 'USA'
        if (str(location)=='Columbus'): location = 'USA'
        if (str(location)=='Dallas'): location = 'USA'
        if (str(location)=='Danville'): location = 'USA'
        if (str(location)=='Florida'): location = 'USA'
        if (str(location)=='Florida, USA'): location = 'USA'
        if (str(location)=='Hollywood'): location = 'USA'
        if (str(location)=='Houston'): location = 'USA'
        if (str(location)=='Houston, TX'): location = 'USA'
        if (str(location)=='Illinois'): location = 'USA'
        if (str(location)=='Indiana'): location = 'USA'
        if (str(location)=='Kentucky'): location = 'USA'
        if (str(location)=='Los Angeles'): location = 'USA'
        if (str(location)=='Los Angeles, CA'): location = 'USA'
        if (str(location)=='Las Vegas'): location = 'USA'
        if (str(location)=='Las Vegas, NV'): location = 'USA'
        if (str(location)=='Louisville'): location = 'USA'
        if (str(location)=='Manhattan'): location = 'USA'
        if (str(location)=='Maryland'): location = 'USA'
        if (str(location)=='Maryland, USA'): location = 'USA'
        if (str(location)=='Marysville'): location = 'USA'
        if (str(location)=='Miami'): location = 'USA'
        if (str(location)=='Miami, FL'): location = 'USA'
        if (str(location)=='New Jersey'): location = 'USA'
        if (str(location)=='New York'): location = 'USA'
        if (str(location)=='New York, NY'): location = 'USA'
        if (str(location)=='New York, USA'): location = 'USA'
        if (str(location)=='North America'): location = 'USA'
        if (str(location)=='North Carolina'): location = 'USA'
        if (str(location)=='NYC'): location = 'USA'
        if (str(location)=='Oakland'): location = 'USA'
        if (str(location)=='Orlando'): location = 'USA'
        if (str(location)=='Orlando, FL'): location = 'USA'
        if (str(location)=='Philadelphia'): location = 'USA'
        if (str(location)=='Queens'): location = 'USA'
        if (str(location)=='San Diego'): location = 'USA'
        if (str(location)=='San Diego, CA'): location = 'USA'
        if (str(location)=='San Francisco'): location = 'USA'
        if (str(location)=='San Francisco, CA'): location = 'USA'
        if (str(location)=='South Carolina'): location = 'USA'
        if (str(location)=='South Carolina, USA'): location = 'USA'
        if (str(location)=='South Dakota'): location = 'USA'
        if (str(location)=='Tampa'): location = 'USA'
        if (str(location)=='Texas'): location = 'USA'
        if (str(location)=='Texas, USA'): location = 'USA'
        if (str(location)=='U.S. '): location = 'USA'
        if (str(location)=='United States'): location = 'USA'
        if (str(location)=='USA'): location = 'USA'
        if (str(location)=='Utah'): location = 'USA'
        if (str(location)=='Virginia'): location = 'USA'
        if (str(location)=='Wellington'): location = 'USA'
        if (str(location)=='Wisconsin'): location = 'USA'

    europe = ['Albania','Andorra','Armenia','Austria','Azerbaijan','Belarus','Belgium','Bosnia and Herzegovina','Bulgaria','Croatia',
             'Czechia','Croydon, London','Cyprus','Denmark','Deutschland','Duisburg, Deutschland', 'Estonia', 'England', 'England, United Kingdom'
             'Liverpool, England', 'London', 'London, England', 'Manchester, England', 'North East, England', 'North West, England',
             'Finland','France','france','Paris, France', 'Saint-Florent-sur-Cher, France', 'Georgia', 'Germany','Greece','Hungary','Iceland','Ireland','Italy',
             'Netherlands', 'The Netherlands', 'Norway','Poland','Portugal','Spain','Sweden','Switzerland','Turkey','Ukraine','United Kingdom',
             'UK']
    
    if (str(location) in europe): location = 'Europe'
    
    if (0==1):
        if (str(location)=='Albania'): location = 'Europe'
        if (str(location)=='Andorra'): location = 'Europe'
        if (str(location)=='Armenia'): location = 'Europe'
        if (str(location)=='Austria'): location = 'Europe'
        if (str(location)=='Azerbaijan'): location = 'Europe'
        if (str(location)=='Belarus'): location = 'Europe'
        if (str(location)=='Belgium'): location = 'Europe'
        if (str(location)=='Bosnia and Herzegovina'): location = 'Europe'
        if (str(location)=='Bulgaria'): location = 'Europe'
        if (str(location)=='Croatia'): location = 'Europe'
        if (str(location)=='Croydon, London'): location = 'Europe'
        if (str(location)=='Cyprus'): location = 'Europe'
        if (str(location)=='Czechia'): location = 'Europe'
        if (str(location)=='Denmark'): location = 'Europe'
        if (str(location)=='Deutschland'): location = 'Europe'
        if (str(location)=='Duisburg, Deutschland'): location = 'Europe'
        if (str(location)=='Estonia'): location = 'Europe'
        if (str(location)=='England'): location = 'Europe'
        if (str(location)=='England, United Kingdom'): location = 'Europe'
        if (str(location)=='Liverpool, England'): location = 'Europe'
        if (str(location)=='London'): location = 'Europe'
        if (str(location)=='London, England'): location = 'Europe'
        if (str(location)=='Manchester, England'): location = 'Europe'
        if (str(location)=='North East, England'): location = 'Europe'
        if (str(location)=='North West, England'): location = 'Europe'
        if (str(location)=='Finland'): location = 'Europe'
        if (str(location)=='France'): location = 'Europe'
        if (str(location)=='france'): location = 'Europe'
        if (str(location)=='Paris, France'): location = 'Europe'
        if (str(location)=='Saint-Florent-sur-Cher, France'): location = 'Europe'
        if (str(location)=='Georgia'): location = 'Europe'
        if (str(location)=='Germany'): location = 'Europe'
        if (str(location)=='Greece'): location = 'Europe'
        if (str(location)=='Hungary'): location = 'Europe'
        if (str(location)=='Iceland'): location = 'Europe'
        if (str(location)=='Ireland'): location = 'Europe'
        if (str(location)=='Italy'): location = 'Europe'
        if (str(location)=='Kazakhstan'): location = 'Europe'
        if (str(location)=='Kosovo'): location = 'Europe'
        if (str(location)=='Latvia'): location = 'Europe'
        if (str(location)=='Liechtenstein'): location = 'Europe'
        if (str(location)=='Lithuania'): location = 'Europe'
        if (str(location)=='Luxembourg'): location = 'Europe'
        if (str(location)=='Malta'): location = 'Europe'
        if (str(location)=='Molova'): location = 'Europe'
        if (str(location)=='Monaco'): location = 'Europe'
        if (str(location)=='Montenegro'): location = 'Europe'
        if (str(location)=='Netherlands'): location = 'Europe'
        if (str(location)=='North Macedonia'): location = 'Europe'
        if (str(location)=='Macedonia'): location = 'Europe'
        if (str(location)=='Norway'): location = 'Europe'
        if (str(location)=='Poland'): location = 'Europe'
        if (str(location)=='Portugal'): location = 'Europe'
        if (str(location)=='Romania'): location = 'Europe'
        if (str(location)=='Russia'): location = 'Europe'
        if (str(location)=='San Marino'): location = 'Europe'
        if (str(location)=='Serbia'): location = 'Europe'
        if (str(location)=='Slovakia'): location = 'Europe'
        if (str(location)=='Slovenia'): location = 'Europe'
        if (str(location)=='Spain'): location = 'Europe'
        if (str(location)=='Sweden'): location = 'Europe'
        if (str(location)=='Switzerland'): location = 'Europe'
        if (str(location)=='Turkey'): location = 'Europe'
        if (str(location)=='Ukraine'): location = 'Europe'
        if (str(location)=='United Kingdom'): location = 'Europe'
        if (str(location)=='UK'): location = 'Europe'
        if (str(location)=='Vatican City'): location = 'Europe'
        
    if (location=='Europe' or location =='USA'):
    
        text = obj.get('text')
        text = text.replace('\t', '').replace('\n', '')

        outfile.write(obj.get('user').get('screen_name')+'\t'+obj.get('created_at')+'\t'+location+'\t'+text+'\n')
        #if (cnt>1000): break

print('done.')

