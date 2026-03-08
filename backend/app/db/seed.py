"""Seeds the database with data currently hardcoded in the frontend JSX files."""

from sqlalchemy import select

from app.db.session import async_session
from app.models.artisan import Artisan
from app.models.product import Product
from app.models.material import Material
from app.core.security import hash_password


async def seed_database():
    """Insert seed data if the database is empty."""
    async with async_session() as db:
        # Check if already seeded
        result = await db.execute(select(Artisan).limit(1))
        if result.scalar_one_or_none() is not None:
            return  # Already seeded

        # ── Artisan (from Profile.jsx + DashboardLayout.jsx) ──────────────
        artisan = Artisan(
            name="Ramesh Kumar",
            mobile="9876543210",
            hashed_password=hash_password("password123"),
            role="Master Weaver",
            location="Jaipur, India",
            member_since="2021",
            bio=(
                "I am a third-generation master weaver based in the heart of Jaipur, "
                "Rajasthan. My family has been dedicated to the intricate art of "
                "Banarasi silk weaving for over seven decades, preserving the traditional "
                "motifs and handloom techniques that have defined our heritage.\n\n"
                "My journey began at the age of 14, learning from my grandfather. "
                "Today, I specialize in combining ancient weaving styles with natural "
                "dyeing processes to create eco-friendly, luxury textiles that tell a story.\n\n"
                "Through ArtisanGPS, I aim to bridge the gap between traditional "
                "craftsmanship and modern market demands, ensuring that the art of "
                "the handloom continues to thrive in the digital age."
            ),
            skills=["Silk Weaving", "Natural Dyeing", "Traditional Loom"],
            avatar_url="/images/ramesh_kumar.png",
            lifetime_earnings="₹4.2L",
            completed_orders=158,
            fulfillment_pct=99,
            market_accuracy=94,
            workshops=24,
            awards=3,
            countries=8,
        )
        db.add(artisan)
        await db.flush()

        # ── Products (from MyCrafts.jsx) ──────────────────────────────────
        products_data = [
            {"name": "Banarasi Silk Saree", "material": "Hand-woven traditional silk", "stock": 12, "price": "₹18,500", "badge": "High Demand", "image_url": "/images/banarasi_saree.jpg", "category": "Textiles"},
            {"name": "Hand-painted Pot", "material": "Organic clay terracotta", "stock": 45, "price": "₹850", "badge": "Stable", "image_url": "/images/terracotta_pot.jpg", "category": "Pottery"},
            {"name": "Brass Dhokra Art", "material": "Lost-wax metal casting", "stock": 8, "price": "₹4,200", "badge": "Growing", "image_url": "/images/brass_dhokra.jpg", "category": "Metalwork"},
            {"name": "Pashmina Shawl", "material": "Premium hand-spun wool", "stock": 5, "price": "₹25,000", "badge": "High Demand", "image_url": "/images/pashmina_shawl.jpg", "category": "Textiles"},
            {"name": "Channapatna Toys", "material": "Lacquered wood craft", "stock": 32, "price": "₹1,250", "badge": "Trending", "image_url": "/images/channapatna_toy.jpg", "category": "Woodwork"},
            {"name": "Jaipur Blue Pottery", "material": "Quartz-based ceramic vase", "stock": 18, "price": "₹3,400", "badge": "High Demand", "image_url": "/images/ceramic_vase.jpg", "category": "Pottery"},
        ]
        for p in products_data:
            db.add(Product(artisan_id=artisan.id, **p))

        # ── Materials (from Constraints.jsx — commodities + mandiData) ────
        materials_data = [
            # Textiles
            {
                "name": "Cotton\nYarn", "price": "₹245", "unit": "/ kg", "change_pct": "-2.4%",
                "trend": "down", "color": "#22c55e", "category": "Textiles",
                "sparkline_points": "0,20 20,25 40,18 60,28 80,22 100,30 120,35",
                "commodity_full_name": "Cotton Yarn (40s)", "sub_unit": "Per kg",
                "local_price": "₹245", "local_best": 0,
                "surat_price": "₹230", "surat_best": 1,
                "delhi_price": "₹240", "delhi_best": 0,
                "action": "Source from Surat",
            },
            {
                "name": "Mulberry\nSilk", "price": "₹4,200", "unit": "/ kg", "change_pct": "+1.8%",
                "trend": "up", "color": "#ef4444", "category": "Textiles",
                "sparkline_points": "0,35 20,30 40,32 60,25 80,20 100,15 120,10",
                "commodity_full_name": "Mulberry Silk", "sub_unit": "Per kg",
                "local_price": "₹4,200", "local_best": 1,
                "surat_price": "₹4,350", "surat_best": 0,
                "delhi_price": "₹4,280", "delhi_best": 0,
                "action": "Buy Local",
            },
            {
                "name": "Zari", "price": "₹850", "unit": "/ spool", "change_pct": "+0.5%",
                "trend": "up", "color": "#ef4444", "category": "Textiles",
                "sparkline_points": "0,30 20,28 40,32 60,29 80,26 100,24 120,22",
                "commodity_full_name": "Zari (Imitation)", "sub_unit": "Per spool",
                "local_price": "₹850", "local_best": 0,
                "surat_price": "₹840", "surat_best": 0,
                "delhi_price": "₹810", "delhi_best": 1,
                "action": "Source from Delhi",
            },
            # Metals
            {
                "name": "Brass\nSheet", "price": "₹580", "unit": "/ kg", "change_pct": "— 0.0%",
                "trend": "flat", "color": "#9ca3af", "category": "Metals",
                "sparkline_points": "0,20 20,21 40,19 60,20 80,21 100,20 120,20",
                "commodity_full_name": "Brass Sheet", "sub_unit": "Per kg",
                "local_price": "₹580", "local_best": 0,
                "surat_price": "₹560", "surat_best": 1,
                "delhi_price": "₹575", "delhi_best": 0,
                "action": "Source from Surat",
            },
            {
                "name": "Copper\nWire", "price": "₹790", "unit": "/ kg", "change_pct": "+3.1%",
                "trend": "up", "color": "#ef4444", "category": "Metals",
                "sparkline_points": "0,38 20,32 40,34 60,28 80,22 100,16 120,8",
                "commodity_full_name": "Copper Wire", "sub_unit": "Per kg",
                "local_price": "₹790", "local_best": 0,
                "surat_price": "₹810", "surat_best": 0,
                "delhi_price": "₹770", "delhi_best": 1,
                "action": "Source from Delhi",
            },
            {
                "name": "Silver\nThread", "price": "₹95", "unit": "/ gram", "change_pct": "-0.2%",
                "trend": "down", "color": "#22c55e", "category": "Metals",
                "sparkline_points": "0,15 20,18 40,16 60,19 80,17 100,20 120,22",
                "commodity_full_name": "Silver Thread", "sub_unit": "Per gram",
                "local_price": "₹95", "local_best": 1,
                "surat_price": "₹98", "surat_best": 0,
                "delhi_price": "₹97", "delhi_best": 0,
                "action": "Buy Local",
            },
        ]
        for m in materials_data:
            db.add(Material(**m))

        await db.commit()
        print("✅ Database seeded successfully!")
