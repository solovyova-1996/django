// window.addEventListener("load", () => {
//     $('.products-admins').on('click', 'input[type="submit"]', function () {
//         let t_href = event.target;
//         // let csrf_token = $('meta[name="csrf-token"]').attr('content')
//         console.log(t_href.name);
//         // console.log(csrf_token)
//
//         // $.ajaxSetup({
//         //     headers: {
//         //         'X-CSRFToken':csrf_token
//         //     }
//         //     });
//
//         $.ajax ({
//             type: 'POST',
//             url: '/admins/products-delete/' + t_href.name + '/',
//             success: function (data) {
//                 $('.table-responsive').html(data.result)
//             },
//         });
//         event.preventDefault()
//     });
//
// }, false);