
const URL = '/api/cupcakes'


$("#cupcake-list").on("click", ".delete-cake", async function (evt) {

	evt.preventDefault();
	const id = $(this).data('id');

	await axios.delete(`${URL}/${id}`);
	$(this).parent().remove();
});


function createCakeDiv(cupcake) {
	return `
	<div class="col-md-4">
		<h3>${cupcake.flavor}</h3>
		${cupcake.size}, ${cupcake.rating}
		<button class="btn btn-secondary btn-sm delete-cake" data-id=${cupcake.id}>delete</button>
		<p><img class="img-fluid mt-3" src="${cupcake.image}" alt=""></p>
	</div>
	`;
}


$("#cupcake-form").on("submit", async function (evt) {

	evt.preventDefault();

	const input_flavor = $('.input-flavor').val();
	const input_size = $('.input-size').val();
	const input_rating = $('.input-rating').val();
	const input_image = $('.input-image').val();

	const resp = await axios.post(URL, {
		flavor: input_flavor,
		size: input_size,
		rating: input_rating,
		image: input_image
	});

	console.log(resp);
	let newCupcake = $(createCakeDiv(resp.data.cupcake));
	$("#cupcake-list").append(newCupcake);
	$("#cupcake-form").trigger("reset");

});
