import { useState } from "react";
import flecha from "../assets/control.png"
import ubL from "../assets/ub_logo.png"
import React from "react";
import {ReactComponent as home} from "../assets/hogar.svg"
import {ReactComponent as calendari} from "../assets/calendar.svg"
import {useNavigate } from 'react-router-dom';


export const Sidebar = () => {
    
    const navigate = useNavigate()
    const [open, setOpen] = useState(false);
    const Menus = [
        { title: "Inici", Image : home, height:"30" , width:"30", style: "fill-white group-hover:fill-sky-500 duration-700", goTo : "/main"},
        { title: "Calendari", Image : calendari, height:"40" , width:"30", style: "stroke-white group-hover:stroke-sky-500 duration-700", goTo : "/"} 
    ];

    return (
        <div className="flex bg-slate-800">
            <div className="w-1/5 p-4">
                <div
                    className={` ${open ? "w-72" : "w-20 "
                        } bg-dark-purple h-screen p-5  pt-8 relative duration-1000`}
                >
                    <img
                        src={flecha}
                        width="50px"
                        height="50px"
                        className={`scale-0 md:scale-150 absolute cursor-pointer -right-7 top-11 w-7 border-sky-500 border-2 rounded-full  ${!open && "rotate-180"}`}
                        onClick={() => setOpen(!open)
                        }
                    />
                    <div className="flex gap-x-4 items-center">
                        <img
                            src={ubL}
                        />
                        <h1
                            className={`text-white origin-left font-medium text-xl duration-1000 ${!open && "scale-0"}`}
                        >
                            Corrector UB
                        </h1>
                    </div>
                    <ul className="pt-6">
                        {Menus.map((Menu, index) => (
                            <li
                                key={index}
                                className={`flex rounded-md p-2 cursor-pointer group  text-gray-300 hover:text-sky-500   text-lg font-bold items-center gap-x-4  ${Menu.gap ? "mt-9" : "mt-2"} ${index === 0 && "bg-light-white"}  `}
                                onClick={(e) => {
                                    navigate(Menu.goTo)
                                }}>
                                <div>
                                <Menu.Image height={Menu.height} width={Menu.width} className={Menu.style} />
                                </div>
                                
                                <div className={`${!open && "scale-0"} origin-left duration-700`}>
                                <span >
                                    {Menu.title}
                                </span>
                                </div>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
};
