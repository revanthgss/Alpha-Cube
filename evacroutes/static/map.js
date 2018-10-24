function GetMap() {
    let content = document.getElementById('content');
    let victims = content.querySelectorAll('.victim');
    let map = new Microsoft.Maps.Map('#myMap', {
        credentials: 'Aqxws6GyR0KaQH-uo9w92nqNeePHAzsbkVDbrpiayIiAwfTbXcML-wj1XLEBPQcQ',
        center: new Microsoft.Maps.Location(10.8505, 76.2711),
        zoom: 7.5
    });
    let tooltipTemplate = `<div style="background-color:white;height:20px;width:150px;padding:5px;text-align:center"><p><b>{title}</b></p><p>{time}</p></div>`;
    //Create an infobox to use as a tooltip when hovering.
    tooltip = new Microsoft.Maps.Infobox(map.getCenter(), {
        visible: false,
        showPointer: false,
        showCloseButton: false,
        offset: new Microsoft.Maps.Point(-75, 10)
    });

    tooltip.setMap(map);
    
    //Create an infobox for displaying detailed information.
    infobox = new Microsoft.Maps.Infobox(map.getCenter(), {
        visible: false
    });

    infobox.setMap(map);
    victims.forEach(victim => {
        let phoneNumber = victim.querySelector('.phone_number').textContent;
        let lat = victim.querySelector('.lat').textContent;
        let lon = victim.querySelector('.lon').textContent;
        let time = victim.querySelector('.time').textContent+" ago";
        let location = new Microsoft.Maps.Location(lat,lon);
        console.log(lat,lon);
        //Create custom Pushpin

        var pin = new Microsoft.Maps.Pushpin(location);

        //Store some metadata with the pushpin.
        pin.metadata = {
            title: phoneNumber,
            description: time
        };

        //Add a click event handler to the pushpin.
        Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked);
        Microsoft.Maps.Events.addHandler(pin, 'mouseover', pushpinHovered);
        Microsoft.Maps.Events.addHandler(pin, 'mouseout', closeTooltip);

        //Add pushpin to the map.
        map.entities.push(pin);
    })
    function pushpinClicked(e) {
        //Make sure the infobox has metadata to display.
        if (e.target.metadata) {
            //Set the infobox options with the metadata of the pushpin.
            infobox.setOptions({
                location: e.target.getLocation(),
                title: e.target.metadata.title,
                description: e.target.metadata.description,
                visible: true
            });
        }
    }
    function pushpinHovered(e) {
        //Hide the infobox
        infobox.setOptions({ visible: false });

        //Make sure the infobox has metadata to display.
        if (e.target.metadata) {
            //Set the infobox options with the metadata of the pushpin.
            tooltip.setOptions({
                location: e.target.getLocation(),
                htmlContent: tooltipTemplate.replace('{title}', e.target.metadata.title).replace('{time}',e.target.metadata.description),
                visible: true
            });
        }
    }

    function closeTooltip() {
        //Close the tooltip.
        tooltip.setOptions({
            visible: false
        });
    }
}