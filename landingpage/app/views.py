from django.shortcuts import render

images = {
        1: 'images/gold-earlings.jpg',
        2: 'images/gold-home.jpg',
        3: 'images/gold-necklace.jpg',
        4: 'images/gold-braclet.jpg',
        5: 'images/gold-ring.jpg',
        6: 'images/silver-earlings.jpg',
    }
describtion={
        1: 'Gold earrings are a timeless and elegant accessory that add a touch of sophistication to any outfit. Crafted from high-quality gold, they come in various designs, from classic hoops to intricate studs. These versatile pieces are perfect for both everyday wear and special occasions. Their enduring appeal makes them a cherished addition to any jewelry collection.',
        2: 'Gold earrings and necklaces are timeless symbols of elegance and sophistication. Gold earrings, available in styles like studs and hoops, offer versatility and a touch of luxury to any outfit. Gold necklaces, ranging from delicate chains to bold statement pieces, enhance both casual and formal looks. Together, these gold accessories create a cohesive, stylish appearance, reflecting the wearers taste and enhancing their overall ensemble. Their enduring beauty ensures they remain cherished accessories for years to come.',
        3: 'Gold necklaces are classic pieces that exude elegance and charm. Whether in a minimalist design or adorned with gemstones, they add a sophisticated touch to any outfit. Their timeless appeal makes them a versatile accessory for both everyday wear and special occasions.',
        4: 'Gold necklaces are classic pieces that exude elegance and charm. Whether in a minimalist design or adorned with gemstones, they add a sophisticated touch to any outfit. Their timeless appeal makes them a versatile accessory for both everyday wear and special occasions.',
        5: 'Gold necklaces are classic pieces that exude elegance and charm. Whether in a minimalist design or adorned with gemstones, they add a sophisticated touch to any outfit. Their timeless appeal makes them a versatile accessory for both everyday wear and special occasions.',
        6: 'Gold necklaces are classic pieces that exude elegance and charm. Whether in a minimalist design or adorned with gemstones, they add a sophisticated touch to any outfit. Their timeless appeal makes them a versatile accessory for both everyday wear and special occasions.',
}

def landing_page(request):
    return render(request, 'app/landing.html')

def card_details(request, post_id):
   
    post_image = images[post_id]
    description_detail=describtion[post_id]
    return render(request, 'app/card_details.html', {
        'post_id': post_id,
        'post_image': post_image,
        'image':post_image,
        'desc':description_detail
        })

def all_post(request):
    return render(request,'app/all_post.html')
