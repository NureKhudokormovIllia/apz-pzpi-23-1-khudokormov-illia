#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

/* Ініціалізація модуля – викликається при завантаженні */
static int __init hello_init(void)
{
    printk(KERN_INFO "Модуль завантажено\n");
    return 0;  /* 0 = успіх */
}

/* Завершення модуля – викликається при вивантаженні */
static void __exit hello_exit(void)
{
    printk(KERN_INFO "Модуль вивантажено\n");
}

module_init(hello_init);
module_exit(hello_exit);

MODULE_LICENSE("GPL");