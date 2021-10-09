// window.onload = function () {
//     $('.products_list').on('click', 'a[class="btn btn-outline-success"]', function () {
//         let t_href = event.target;
//         console.log(t_href);
//         console.log(t_href.name);
//         console.log(t_href.value);
//
//         $.ajax({
//             url: '/products/products_list/'+ 2 + '/',
//             success: function (data) {
//                 $('.products_list').html(data.result)
//             },
//         });
//         event.preventDefault()
//     });
//
// };