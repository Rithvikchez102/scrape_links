// // Get all anchor tags
// const links = [...document.querySelectorAll('a[href]')];

// // Filter links that contain "/need/detail/?need_id="
// const filteredLinks = links
//   .map(a => a.href)
//   .filter(href => href.includes('/need/detail/?need_id='));

// // Log the result
// console.log(filteredLinks);


function filter_function(href, pattern_inclue, pattern_exclude) {


  if (pattern_inclue && pattern_exclude) {
    return href.includes(pattern_inclue) && !href.includes(pattern_exclude);
  }
  else if (pattern_inclue) {
    return href.includes(pattern_inclue);
  } else if (pattern_exclude) {
    return !href.includes(pattern_exclude);
  } else {
    console.log('No patterns provided');
  }
}

function get_links(pattern_include, pattern_exclude) {
  // Get all anchor tags
  console.log('get_links called with pattern:', pattern_include, pattern_exclude); 
  const links = [...document.querySelectorAll('a[href]')];

  // Filter links that contain "/need/detail/?need_id="
  const filteredLinks = links
    .map(a => a.href)
    .filter(href => filter_function(href, pattern_include, pattern_exclude));

  // Log the result
  console.log(filteredLinks);

  return filteredLinks;
}