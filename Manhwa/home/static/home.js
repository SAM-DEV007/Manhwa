window.onload = function(){
    const obj = JSON.parse(data);

    const container = document.getElementById('container');

    for (let i = 0; i < obj.types.length; i++) {
        let current = obj.types[i];

        let subhead = document.createElement('h2');
        subhead.innerHTML = current.title;
        container.appendChild(subhead);

        let subdesc = document.createElement('p');
        subdesc.innerHTML = current.desc;
        container.appendChild(subdesc);

        for (let j = 0; j < current.list.length; j++) {
            let list_current = current.list[j];

            let ul = document.createElement('ul');

            let h3 = document.createElement('h3');
            h3.innerHTML = list_current.title;
            ul.appendChild(h3);

            let img = document.createElement('img');
            img.src = `https://${file_location}/Images/${list_current.img_name}`;
            img.alt = list_current.title.slice(3);
            ul.appendChild(img);

            for (let k = 0; k < list_current.points.length; k++) {
                let li = document.createElement('li')
                li.innerHTML = list_current.points[k];
                ul.appendChild(li);
            }

            let p = document.createElement('p');
            p.innerHTML = list_current.desc;
            ul.appendChild(p);

            container.appendChild(ul);
        }
    }
};