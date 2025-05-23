export async function GET() {
  try {
    const response = await fetch('https://world.openfoodfacts.org/category/cheeses.json');
    if (!response.ok) {
      return new Response('Failed to fetch cheese data', { status: 500 });
    }
    const data = await response.json();
    const cheeses = (data.products || []).map(p => ({
      name: p.product_name,
      brands: p.brands,
      image: p.image_front_url
    }));
    return Response.json({ cheeses });
  } catch (err) {
    return new Response('Error retrieving cheese data', { status: 500 });
  }
}
