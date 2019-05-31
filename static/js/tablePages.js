$(document).ready(function() {
	$('.table').footable({
		'paging': {
			'size': 10,
			'enabled': true
		},
		'sorting': {
			'enabled': true
		}
	});

	// $('#pages').DataTable({
	// 	'pageLength': 10,
	// 	'info': false,
	// 	'searching': false,
	// 	'lengthChange': false,
	// 	'language': {
	// 		'paginate': {
	// 			'previous': '<',
	// 			'next': '>'
	// 		}
	// 	},
	// })
});