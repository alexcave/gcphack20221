
/*  ==========================================
    SHOW UPLOADED IMAGE
* ==========================================

 https://jsfiddle.net/bootstrapious/8w7a50n2/ */

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$(function () {
    $('#upload').on('change', function () {
        readURL(input);
    });
});

// $(function () {
//     $('#email-address').change(function () {
//         console.log('change')
//         bootstrapValidate('#email-address', 'email|required', function (isValid) {
//             console.log(isValid)
//             console.log('in fnc')
//         if (isValid) {
//             console.log('valid email')
//             // $('#create-avatar-btn').removeClass('disabled');
//         } else {
//             console.log('invalid email')
//             // $('#create-avatar-btn').addClass('disabled');
//         }
//     })
//     });
// });

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById( 'upload' );
var infoArea = document.getElementById( 'upload-label' );

input.addEventListener( 'change', showFileName );
function showFileName( event ) {
  var input = event.target;
  var fileName = input.files[0].name;
  infoArea.textContent = fileName;
}
