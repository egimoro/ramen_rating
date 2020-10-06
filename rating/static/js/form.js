$('#getRating').bind('click', ()=>{
  
        alert('Here are your ratings!');
        loadData();
        
   
    
});


Add = ()=>{
    var formData = {
        brand: $('#id_brand').val(),
        variety: $('#id_variety').val(),
        style: $('#id_style').val(),
        country: $('#id_country').val(),
        dateReview: $('#id_dateReview').val(),
        stars: $('#id_stars').val(),
        topTen: $('#id_topTen').val()




    };

    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: '/rating/add/',
        type: 'POST',
        data: formData,
        dataType: 'json',
        success: (data) =>{
            loadData();
            $('#myModal').modal('hide');
            alert('Rating successfully added!');
            console.log(data);
            
        },
        error: (errormessage) =>{
            alert(errormessage.responseText);
        }

    });

};


 getCookie=(name)=> {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


loadData = () =>{
    $.ajax({

        url: '/rating/list',
        type: 'GET',
        dataType: 'json',
        success: (data) =>{
            var row = '';
            $.each(data.rating_list, (i, ramen)=>{
                row += `
                    <tr id="ramen-${ramen.id}">
                     <td>${ramen.id}</td>
                     <td class="r_brand">${ramen.brand}</td>
                     <td class="r_variety">${ramen.variety}</td>
                     <td class="r_variety">${ramen.style}</td>
                     <td class="r_country">${ramen.country}</td>
                     <td class="r_stars">${ramen.stars}</td>
                     <td class="r_dateReview">${ramen.dateReview}</td>
                     <td class="r_topTen">${ramen.topTen}</td>
                     <td>
                        <button class="btn btn-primary" onclick="getDetail(${ramen.id})">Edit</button>
                        <button class="btn btn-danger" onclick="Delete(${ramen.id})">Delete</button>
                     </td>

                    <tr>
                `  
            });
            $('#ramenTable tbody').append(row);
            console.log(data);
            setInterval('refreshPage()', 90000);
        },
        error: (errormessage) =>{
            alert(errormessage.responseText);
        }

    });
};

refreshPage = () => {
    location.reload();
};


getDetail = (id) =>{

    $.ajax({

        url: '/rating/' + id,
        type: 'GET',
        dataType: 'json',
        success: (data)=>{
            $('#id_formram').val(data.rating.id);
            $('#id_brand').val(data.rating.brand);
            $('#id_variety').val(data.rating.variety);
            $('#id_style').val(data.rating.style);
            $('#id_country').val(data.rating.country);
            $('#id_stars').val(data.rating.stars);
            $('#id_dateReview').val(data.rating.dateReview);
            $('#id_topTen').val(data.rating.topTen);

            $('#myModal').modal('show');
            $('#btnUpdate').show();
            $('#btnAdd').hide();
            console.log(data);
        },
        error: (errormessage) =>{
            alert(errormessage.responseText);
        }

    });

};

Update = () =>{

    var id = $('#id_formram').val()

    var formData = {

        brand: $('#id_brand').val(),
        variety: $('#id_variety').val(),
        style: $('#id_style').val(),
        country: $('#id_country').val(),
        dateReview: $('#id_dateReview').val(),
        stars: $('#id_stars').val(),
        topTen: $('#id_topTen').val()


    };

    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: '/rating/update/' + id,
        data: formData,
        type: 'POST',
        dataType: 'json',
        success: (data) =>{
            loadData();
            $('#myModal').modal('hide');
            $('#id_brand').val('');
            $('#id_variety').val('');
            $('#id_style').val('');
            $('#id_stars').val('');
            $('#id_dateReview').val('');
            $('#id_topTen').val('');
            alert('Rating updated!');
        },
        error: (errormessage) =>{
            alert(errormessage.responseText);
        }

    });
    

};

Delete = (id) =>{

    var ans = confirm('Are you sure you want to delete this Rating?');
    
    if (ans) {

        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: '/rating/delete/' + id,
            type: 'POST',
            dataType: 'json',
            success: (data) =>{
                loadData();
            }

        });
        
    };

};