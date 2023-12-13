import React from 'react';
import SidebarOption from "./SidebarOption";
import styled from "styled-components";
import FiberManualRecordIcon from "@mui/icons-material/FiberManualRecord";
import CreateIcon from "@mui/icons-material/Create";
import InsertCommentIcon from "@mui/icons-material/InsertComment"
import InboxIcon from "@mui/icons-material/Inbox";
import DraftsIcon from "@mui/icons-material/Drafts";
import BookmarkBorderIcon from "@mui/icons-material/BookmarkBorder";
import FileCopyIcon from "@mui/icons-material/FileCopy";
import PeopleAltIcon from "@mui/icons-material/PeopleAlt";
import AppsIcon from "@mui/icons-material/Apps";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import  ExpandLessIcon from "@mui/icons-material/ExpandLess";
import AddIcon from "@mui/icons-material/Add";

function SideBar() {
    return (
        <SideBarContainer>
            <SideBarHeader>
                <SideBarInfo>
                    <h2>Merkey </h2>
                    <h3>
                      <FiberManualRecordIcon />
                      Nathan Di
                    </h3>
                </SideBarInfo>
                <CreateIcon />
            </SideBarHeader>

            <SidebarOption Icon={InsertCommentIcon} title="Treads" />
            <SidebarOption Icon={InboxIcon} title="Mention & reactions" />
            <SidebarOption Icon={DraftsIcon} title="Saved item" />
            <SidebarOption Icon={BookmarkBorderIcon} title="Channel browser" />
            <SidebarOption Icon={FileCopyIcon} title="People & user group" />
            <SidebarOption Icon={PeopleAltIcon} title="Apps" />
            <SidebarOption Icon={AppsIcon} title="File browser" />
            <SidebarOption Icon={ExpandMoreIcon} title="Channels" />
            <SidebarOption Icon={ExpandLessIcon} title="Show less" />
            <hr/>
            <SidebarOption Icon={AddIcon} title="Add" />

        </SideBarContainer>
    )
}

export default SideBar;

const SideBarContainer = styled.div`
    background-color: var(--slack-color);
    color: white;
    //flex: 0.3;
    border-top: 1px solid #4927Ab;
    max-width: 260px;
    margin-top: 60px;
    width: 200px;
`
const SideBarHeader = styled.div`
    display: flex;
    border-bottom: 1px solid #4927Ab;
    padding:13px;
    
    > .MuiSvgIcon-root {
        padding: 8px;
        color: #4927Ab;
        font-size: 18px;
        background-color: white;
        border-radius: 99px
    }
`
const SideBarInfo = styled.div`
       flex: 1;
       > h2{
        font-size: 15px;
        font-weight: 900;
        margin-bottom: 5px;
       }
       > h3{
        display: flex;
        font-size: 13px;
        font-weight: 400;
        align-item: center;
       }
       > h3 > .MuiSvgIcon-root {
        font-size: 14px;
        margin-top: 1px;
        margin-right: 2px;
        color: green;
       }
`
