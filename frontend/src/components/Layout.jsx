import { Outlet, useLocation } from "react-router-dom";
import BottomNav from "./BottomNav";

export default function Layout() {
  const location = useLocation();
  const isLandingPage = location.pathname === "/";

  return (
    <div className={`app-container ${!isLandingPage ? "pb-nav" : ""}`}>
      <main>
        <Outlet />
      </main>
      {!isLandingPage && <BottomNav />}
    </div>
  );
}
