$(document).ready(function() {
	flashed_messages();


	/* -- Adds a new "Ingredient" input field in form on Edit Recipe/Add Recipe page --*/

	$('#new-ingredient').on('click', function() {
		$('<div class="input-group add-on ingredient-block" id="ingredient-block"><input type="text" class="form-control ingredient" name="ingredient" id="ingredient" placeholder="Add New Ingredient"><div class="input-group-append"><button type="button" class="btn btn-danger delete-ingredient-button">Delete</button></div>').insertBefore('#new-ingredient');
	});
	
	/* -- Deletes an ingredient input field in form on Edit Recipe/Add Recipe page --*/
	$('.delete-ingredient-button').on('click', function() {
		$(this).closest('.ingredient-block').remove();
	});


	/* -- Adds a new "Tag" input field in form on Edit Recipe/Add Recipe page --*/
	$('.new-tag-button').on('click', function() {
		$('<div class="input-group add-on tag-block"><input type="text" class="form-control" name="tags" placeholder="Add New Tag"><div class="input-group-append" ><button type="button" class="btn btn-danger" id="">Delete</button></div>').insertBefore('.new-tag-button');
	});

	/* -- Deletes "Tag" input field in form on Edit Recipe/Add Recipe page --*/
	$('.delete-tag-button').on('click', function() {
		$(this).closest('.tag-block').remove();
	});

});
/*
Alerts modal
*/

function flashed_messages() {
	let messages = parseInt($("#messages p").length);
	if (messages) {
		$("#alerts").slideDown(1500);
		setTimeout(() => {
			$("#alerts").slideUp(1500);
		}, 7000);
	}
}
