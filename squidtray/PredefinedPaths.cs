﻿using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Diladele.Squid.Tray
{
    static class PredefinedPaths
    {
        private static string installationFolder;

        public static string InstallationFolder
        {
            get 
            {
                if (installationFolder == null)
                {
                    const string basepathStr = @"Software\Squid";

                    using (RegistryKey key = Registry.LocalMachine.OpenSubKey(basepathStr))
                    {
                        if (key == null)
                        {
                            installationFolder = string.Empty;
                        }
                        else
                        {
                            installationFolder = key.GetValue("InstallDir") as string;
                        }
                    }
                }

                return installationFolder;
            }
        }
    }
}
