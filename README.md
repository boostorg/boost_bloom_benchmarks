# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.66</td>
    <td align="right">4.75</td>
    <td align="right">3.74</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.40</td>
    <td align="right">9.82</td>
    <td align="right">15.85</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.74</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.61</td>
    <td align="right">4.79</td>
    <td align="right">4.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.21</td>
    <td align="right">14.60</td>
    <td align="right">17.00</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.57</td>
    <td align="right">4.69</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.17</td>
    <td align="right">5.25</td>
    <td align="right">5.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.42</td>
    <td align="right">17.98</td>
    <td align="right">16.08</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.19</td>
    <td align="right">5.10</td>
    <td align="right">5.14</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.99</td>
    <td align="right">6.06</td>
    <td align="right">6.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">25.90</td>
    <td align="right">22.73</td>
    <td align="right">16.62</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.29</td>
    <td align="right">5.96</td>
    <td align="right">5.78</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.56</td>
    <td align="right">6.44</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">10.14</td>
    <td align="right">10.30</td>
    <td align="right">16.22</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">3.73</td>
    <td align="right">4.12</td>
    <td align="right">4.16</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.41</td>
    <td align="right">4.95</td>
    <td align="right">4.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.25</td>
    <td align="right">15.29</td>
    <td align="right">17.36</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.25</td>
    <td align="right">4.98</td>
    <td align="right">5.04</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">5.12</td>
    <td align="right">5.55</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.18</td>
    <td align="right">18.75</td>
    <td align="right">16.83</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">4.83</td>
    <td align="right">5.43</td>
    <td align="right">5.40</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.47</td>
    <td align="right">6.19</td>
    <td align="right">6.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">22.97</td>
    <td align="right">23.55</td>
    <td align="right">16.97</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.22</td>
    <td align="right">6.13</td>
    <td align="right">6.28</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">6.16</td>
    <td align="right">6.69</td>
    <td align="right">6.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">4.94</td>
    <td align="right">5.11</td>
    <td align="right">5.09</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.17</td>
    <td align="right">5.92</td>
    <td align="right">6.14</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.81</td>
    <td align="right">3.07</td>
    <td align="right">3.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.63</td>
    <td align="right">7.90</td>
    <td align="right">7.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.73</td>
    <td align="right">9.33</td>
    <td align="right">9.27</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.37</td>
    <td align="right">3.00</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.01</td>
    <td align="right">12.71</td>
    <td align="right">12.73</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.70</td>
    <td align="right">13.39</td>
    <td align="right">13.29</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.58</td>
    <td align="right">5.56</td>
    <td align="right">3.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.64</td>
    <td align="right">14.74</td>
    <td align="right">14.74</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.64</td>
    <td align="right">16.84</td>
    <td align="right">16.65</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.68</td>
    <td align="right">5.64</td>
    <td align="right">3.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.56</td>
    <td align="right">5.20</td>
    <td align="right">5.15</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">5.46</td>
    <td align="right">6.03</td>
    <td align="right">6.00</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.90</td>
    <td align="right">2.78</td>
    <td align="right">2.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">5.86</td>
    <td align="right">8.12</td>
    <td align="right">8.12</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">7.18</td>
    <td align="right">9.35</td>
    <td align="right">9.39</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.42</td>
    <td align="right">2.63</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">8.91</td>
    <td align="right">12.00</td>
    <td align="right">12.08</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.85</td>
    <td align="right">13.88</td>
    <td align="right">13.84</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.54</td>
    <td align="right">5.79</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">10.84</td>
    <td align="right">14.21</td>
    <td align="right">14.25</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">12.10</td>
    <td align="right">16.69</td>
    <td align="right">16.72</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.62</td>
    <td align="right">6.01</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.78</td>
    <td align="right">3.03</td>
    <td align="right">3.00</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.13</td>
    <td align="right">4.71</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.27</td>
    <td align="right">4.62</td>
    <td align="right">4.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.90</td>
    <td align="right">3.16</td>
    <td align="right">3.13</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.02</td>
    <td align="right">4.27</td>
    <td align="right">4.25</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.24</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.21</td>
    <td align="right">5.28</td>
    <td align="right">3.67</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">6.75</td>
    <td align="right">7.44</td>
    <td align="right">5.73</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.64</td>
    <td align="right">7.29</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.32</td>
    <td align="right">5.38</td>
    <td align="right">3.71</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.83</td>
    <td align="right">8.80</td>
    <td align="right">5.85</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.17</td>
    <td align="right">8.80</td>
    <td align="right">5.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">2.90</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.26</td>
    <td align="right">4.42</td>
    <td align="right">4.45</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.33</td>
    <td align="right">4.45</td>
    <td align="right">4.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.06</td>
    <td align="right">2.72</td>
    <td align="right">2.72</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.09</td>
    <td align="right">3.87</td>
    <td align="right">3.89</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.37</td>
    <td align="right">4.54</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.24</td>
    <td align="right">5.53</td>
    <td align="right">3.75</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">7.33</td>
    <td align="right">7.70</td>
    <td align="right">5.86</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">7.63</td>
    <td align="right">7.42</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.29</td>
    <td align="right">5.58</td>
    <td align="right">3.72</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.91</td>
    <td align="right">9.00</td>
    <td align="right">5.93</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">8.21</td>
    <td align="right">8.71</td>
    <td align="right">5.73</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">32.69</td>
    <td align="right">20.41</td>
    <td align="right">9.37</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.16</td>
    <td align="right">13.19</td>
    <td align="right">17.92</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.81</td>
    <td align="right">5.30</td>
    <td align="right">5.05</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.85</td>
    <td align="right">6.30</td>
    <td align="right">6.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">24.21</td>
    <td align="right">21.79</td>
    <td align="right">19.13</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.41</td>
    <td align="right">9.27</td>
    <td align="right">8.54</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.59</td>
    <td align="right">6.88</td>
    <td align="right">9.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.99</td>
    <td align="right">28.86</td>
    <td align="right">22.80</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">19.10</td>
    <td align="right">18.86</td>
    <td align="right">17.35</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">17.52</td>
    <td align="right">11.11</td>
    <td align="right">10.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">87.50</td>
    <td align="right">92.48</td>
    <td align="right">32.16</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">25.64</td>
    <td align="right">21.77</td>
    <td align="right">21.87</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">23.01</td>
    <td align="right">20.52</td>
    <td align="right">23.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">13.37</td>
    <td align="right">13.63</td>
    <td align="right">18.53</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.82</td>
    <td align="right">5.62</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">5.42</td>
    <td align="right">6.06</td>
    <td align="right">5.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">21.57</td>
    <td align="right">20.58</td>
    <td align="right">20.62</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">7.72</td>
    <td align="right">9.16</td>
    <td align="right">8.22</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">7.16</td>
    <td align="right">11.97</td>
    <td align="right">15.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">44.67</td>
    <td align="right">49.18</td>
    <td align="right">25.87</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">15.40</td>
    <td align="right">13.48</td>
    <td align="right">15.66</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">15.57</td>
    <td align="right">11.72</td>
    <td align="right">14.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">114.14</td>
    <td align="right">112.48</td>
    <td align="right">33.21</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">22.99</td>
    <td align="right">24.81</td>
    <td align="right">24.70</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">25.15</td>
    <td align="right">25.33</td>
    <td align="right">26.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.01</td>
    <td align="right">7.75</td>
    <td align="right">7.49</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.01</td>
    <td align="right">8.27</td>
    <td align="right">8.75</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.61</td>
    <td align="right">4.14</td>
    <td align="right">4.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.86</td>
    <td align="right">16.77</td>
    <td align="right">10.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">18.57</td>
    <td align="right">26.01</td>
    <td align="right">27.42</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.74</td>
    <td align="right">4.17</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">21.39</td>
    <td align="right">34.44</td>
    <td align="right">38.10</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">34.80</td>
    <td align="right">37.47</td>
    <td align="right">23.93</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">15.10</td>
    <td align="right">15.09</td>
    <td align="right">10.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">31.83</td>
    <td align="right">29.21</td>
    <td align="right">30.46</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">26.55</td>
    <td align="right">27.88</td>
    <td align="right">28.00</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">19.35</td>
    <td align="right">19.93</td>
    <td align="right">13.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">5.87</td>
    <td align="right">8.42</td>
    <td align="right">8.67</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">6.95</td>
    <td align="right">8.45</td>
    <td align="right">8.75</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.77</td>
    <td align="right">3.71</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">9.27</td>
    <td align="right">21.99</td>
    <td align="right">20.12</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">20.97</td>
    <td align="right">24.88</td>
    <td align="right">22.20</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">4.01</td>
    <td align="right">3.62</td>
    <td align="right">4.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">16.11</td>
    <td align="right">21.83</td>
    <td align="right">16.93</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">23.82</td>
    <td align="right">22.58</td>
    <td align="right">25.87</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">20.90</td>
    <td align="right">21.10</td>
    <td align="right">15.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">40.42</td>
    <td align="right">40.21</td>
    <td align="right">36.97</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">36.98</td>
    <td align="right">40.89</td>
    <td align="right">40.43</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">17.72</td>
    <td align="right">19.20</td>
    <td align="right">15.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.56</td>
    <td align="right">4.04</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.56</td>
    <td align="right">6.75</td>
    <td align="right">6.36</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.48</td>
    <td align="right">6.21</td>
    <td align="right">6.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">4.05</td>
    <td align="right">4.80</td>
    <td align="right">4.36</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">4.49</td>
    <td align="right">5.85</td>
    <td align="right">7.52</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">6.48</td>
    <td align="right">7.60</td>
    <td align="right">8.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.85</td>
    <td align="right">20.83</td>
    <td align="right">14.77</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">13.47</td>
    <td align="right">18.61</td>
    <td align="right">12.18</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">13.28</td>
    <td align="right">14.34</td>
    <td align="right">14.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">14.24</td>
    <td align="right">17.38</td>
    <td align="right">12.80</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">23.73</td>
    <td align="right">24.79</td>
    <td align="right">13.83</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">22.26</td>
    <td align="right">32.05</td>
    <td align="right">20.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.76</td>
    <td align="right">3.52</td>
    <td align="right">3.49</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">5.64</td>
    <td align="right">5.82</td>
    <td align="right">5.81</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.48</td>
    <td align="right">5.73</td>
    <td align="right">5.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">4.20</td>
    <td align="right">4.11</td>
    <td align="right">3.96</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">7.18</td>
    <td align="right">5.88</td>
    <td align="right">5.35</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">5.61</td>
    <td align="right">6.31</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">12.70</td>
    <td align="right">11.80</td>
    <td align="right">8.62</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">12.96</td>
    <td align="right">17.72</td>
    <td align="right">13.94</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">16.50</td>
    <td align="right">22.16</td>
    <td align="right">14.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">12.83</td>
    <td align="right">13.01</td>
    <td align="right">10.68</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.84</td>
    <td align="right">23.56</td>
    <td align="right">15.29</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">17.01</td>
    <td align="right">18.97</td>
    <td align="right">13.08</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.31</td>
    <td align="right">3.94</td>
    <td align="right">3.31</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.24</td>
    <td align="right">9.18</td>
    <td align="right">15.46</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.34</td>
    <td align="right">3.97</td>
    <td align="right">3.98</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.86</td>
    <td align="right">7.18</td>
    <td align="right">4.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.09</td>
    <td align="right">14.26</td>
    <td align="right">16.82</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.85</td>
    <td align="right">4.61</td>
    <td align="right">4.66</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.47</td>
    <td align="right">5.28</td>
    <td align="right">5.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.11</td>
    <td align="right">16.43</td>
    <td align="right">15.58</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.32</td>
    <td align="right">5.08</td>
    <td align="right">5.07</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.91</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.76</td>
    <td align="right">20.76</td>
    <td align="right">16.17</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.79</td>
    <td align="right">5.84</td>
    <td align="right">5.85</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.81</td>
    <td align="right">3.27</td>
    <td align="right">3.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">10.22</td>
    <td align="right">9.87</td>
    <td align="right">16.39</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">4.21</td>
    <td align="right">4.22</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.00</td>
    <td align="right">4.90</td>
    <td align="right">4.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.26</td>
    <td align="right">15.28</td>
    <td align="right">17.54</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.65</td>
    <td align="right">4.72</td>
    <td align="right">4.71</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">4.63</td>
    <td align="right">5.64</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.60</td>
    <td align="right">18.08</td>
    <td align="right">16.48</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">5.13</td>
    <td align="right">5.24</td>
    <td align="right">5.24</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.17</td>
    <td align="right">6.08</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">23.67</td>
    <td align="right">22.69</td>
    <td align="right">16.79</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.61</td>
    <td align="right">6.12</td>
    <td align="right">5.92</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">3.16</td>
    <td align="right">3.49</td>
    <td align="right">3.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.03</td>
    <td align="right">3.57</td>
    <td align="right">3.57</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.15</td>
    <td align="right">3.49</td>
    <td align="right">3.49</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.57</td>
    <td align="right">2.47</td>
    <td align="right">2.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.70</td>
    <td align="right">3.36</td>
    <td align="right">3.36</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.73</td>
    <td align="right">3.69</td>
    <td align="right">3.70</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.13</td>
    <td align="right">2.26</td>
    <td align="right">2.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.58</td>
    <td align="right">6.17</td>
    <td align="right">6.16</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.74</td>
    <td align="right">6.06</td>
    <td align="right">6.06</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.16</td>
    <td align="right">4.36</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.97</td>
    <td align="right">6.71</td>
    <td align="right">6.58</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.32</td>
    <td align="right">6.98</td>
    <td align="right">7.20</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.22</td>
    <td align="right">4.38</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.19</td>
    <td align="right">3.77</td>
    <td align="right">3.78</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">3.32</td>
    <td align="right">3.68</td>
    <td align="right">3.87</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.88</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">3.38</td>
    <td align="right">3.67</td>
    <td align="right">3.67</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.89</td>
    <td align="right">3.99</td>
    <td align="right">3.99</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.78</td>
    <td align="right">2.57</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.83</td>
    <td align="right">6.49</td>
    <td align="right">6.51</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">5.87</td>
    <td align="right">6.66</td>
    <td align="right">6.65</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">4.50</td>
    <td align="right">4.72</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">6.27</td>
    <td align="right">6.76</td>
    <td align="right">6.94</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">6.61</td>
    <td align="right">7.19</td>
    <td align="right">7.18</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">4.54</td>
    <td align="right">4.79</td>
    <td align="right">3.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.59</td>
    <td align="right">2.35</td>
    <td align="right">2.34</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.66</td>
    <td align="right">4.09</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.69</td>
    <td align="right">3.93</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.69</td>
    <td align="right">2.42</td>
    <td align="right">2.39</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.95</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.84</td>
    <td align="right">4.02</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.24</td>
    <td align="right">4.30</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.68</td>
    <td align="right">6.10</td>
    <td align="right">4.64</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.84</td>
    <td align="right">6.01</td>
    <td align="right">4.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.28</td>
    <td align="right">4.31</td>
    <td align="right">2.94</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.64</td>
    <td align="right">7.17</td>
    <td align="right">4.81</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.78</td>
    <td align="right">7.01</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">2.80</td>
    <td align="right">2.66</td>
    <td align="right">2.66</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">3.84</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">3.91</td>
    <td align="right">4.32</td>
    <td align="right">4.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">2.95</td>
    <td align="right">2.73</td>
    <td align="right">2.72</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.63</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.13</td>
    <td align="right">4.36</td>
    <td align="right">4.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.52</td>
    <td align="right">4.62</td>
    <td align="right">3.20</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">5.92</td>
    <td align="right">6.46</td>
    <td align="right">4.98</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">5.98</td>
    <td align="right">6.31</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">4.50</td>
    <td align="right">4.62</td>
    <td align="right">3.20</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.11</td>
    <td align="right">7.54</td>
    <td align="right">5.18</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">7.04</td>
    <td align="right">7.34</td>
    <td align="right">5.00</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.06</td>
    <td align="right">14.73</td>
    <td align="right">5.77</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.09</td>
    <td align="right">10.82</td>
    <td align="right">16.49</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.98</td>
    <td align="right">4.64</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.59</td>
    <td align="right">5.33</td>
    <td align="right">5.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.48</td>
    <td align="right">16.16</td>
    <td align="right">17.58</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.40</td>
    <td align="right">5.09</td>
    <td align="right">5.10</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.17</td>
    <td align="right">5.95</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">19.06</td>
    <td align="right">19.13</td>
    <td align="right">16.38</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.26</td>
    <td align="right">5.93</td>
    <td align="right">5.95</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.72</td>
    <td align="right">6.76</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">31.45</td>
    <td align="right">31.54</td>
    <td align="right">17.33</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">6.20</td>
    <td align="right">7.03</td>
    <td align="right">6.96</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.17</td>
    <td align="right">4.70</td>
    <td align="right">4.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">11.95</td>
    <td align="right">12.06</td>
    <td align="right">17.52</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">5.01</td>
    <td align="right">4.91</td>
    <td align="right">4.82</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">4.72</td>
    <td align="right">5.57</td>
    <td align="right">5.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">17.16</td>
    <td align="right">17.52</td>
    <td align="right">18.29</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="right">5.28</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">5.25</td>
    <td align="right">6.22</td>
    <td align="right">6.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">22.55</td>
    <td align="right">23.32</td>
    <td align="right">17.44</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">6.15</td>
    <td align="right">6.13</td>
    <td align="right">6.10</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">5.96</td>
    <td align="right">7.00</td>
    <td align="right">6.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">29.22</td>
    <td align="right">21.29</td>
    <td align="right">16.29</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">7.13</td>
    <td align="right">7.37</td>
    <td align="right">7.34</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">4.35</td>
    <td align="right">4.81</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.69</td>
    <td align="right">4.34</td>
    <td align="right">4.34</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.78</td>
    <td align="right">4.27</td>
    <td align="right">4.28</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.09</td>
    <td align="right">3.09</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.18</td>
    <td align="right">3.89</td>
    <td align="right">3.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.11</td>
    <td align="right">4.29</td>
    <td align="right">4.29</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.54</td>
    <td align="right">2.70</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.84</td>
    <td align="right">7.35</td>
    <td align="right">7.34</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">6.98</td>
    <td align="right">7.64</td>
    <td align="right">7.63</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">4.84</td>
    <td align="right">5.26</td>
    <td align="right">3.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">7.61</td>
    <td align="right">8.70</td>
    <td align="right">8.61</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">7.68</td>
    <td align="right">9.00</td>
    <td align="right">9.10</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">5.68</td>
    <td align="right">6.12</td>
    <td align="right">4.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">3.86</td>
    <td align="right">4.54</td>
    <td align="right">4.56</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">3.95</td>
    <td align="right">4.48</td>
    <td align="right">4.52</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.46</td>
    <td align="right">3.42</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.95</td>
    <td align="right">4.24</td>
    <td align="right">4.24</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.34</td>
    <td align="right">4.67</td>
    <td align="right">4.67</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.26</td>
    <td align="right">3.05</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">7.41</td>
    <td align="right">8.35</td>
    <td align="right">8.36</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">7.01</td>
    <td align="right">8.08</td>
    <td align="right">8.07</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">5.34</td>
    <td align="right">5.85</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">7.97</td>
    <td align="right">8.92</td>
    <td align="right">8.96</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">8.42</td>
    <td align="right">9.48</td>
    <td align="right">9.48</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">5.85</td>
    <td align="right">6.40</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.11</td>
    <td align="right">2.96</td>
    <td align="right">2.97</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.31</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.37</td>
    <td align="right">4.79</td>
    <td align="right">4.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.08</td>
    <td align="right">2.97</td>
    <td align="right">2.95</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.42</td>
    <td align="right">4.31</td>
    <td align="right">4.32</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.31</td>
    <td align="right">4.70</td>
    <td align="right">4.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">4.81</td>
    <td align="right">5.11</td>
    <td align="right">3.62</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.87</td>
    <td align="right">7.61</td>
    <td align="right">6.09</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">6.97</td>
    <td align="right">7.52</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">5.66</td>
    <td align="right">6.04</td>
    <td align="right">4.31</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">8.48</td>
    <td align="right">9.35</td>
    <td align="right">6.68</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">8.68</td>
    <td align="right">9.36</td>
    <td align="right">6.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.38</td>
    <td align="right">3.32</td>
    <td align="right">3.33</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.57</td>
    <td align="right">5.26</td>
    <td align="right">5.25</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">4.64</td>
    <td align="right">5.22</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.37</td>
    <td align="right">3.31</td>
    <td align="right">3.31</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">4.20</td>
    <td align="right">4.68</td>
    <td align="right">4.66</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">4.46</td>
    <td align="right">4.83</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">5.19</td>
    <td align="right">5.59</td>
    <td align="right">4.00</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">7.12</td>
    <td align="right">8.14</td>
    <td align="right">6.59</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">7.16</td>
    <td align="right">7.85</td>
    <td align="right">6.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">6.16</td>
    <td align="right">6.70</td>
    <td align="right">4.83</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.66</td>
    <td align="right">9.43</td>
    <td align="right">6.88</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">9.15</td>
    <td align="right">9.87</td>
    <td align="right">7.01</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">22.18</td>
    <td align="right">4.65</td>
    <td align="right">3.63</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.04</td>
    <td align="right">6.91</td>
    <td align="right">16.05</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.44</td>
    <td align="right">1.32</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.89</td>
    <td align="right">1.90</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.49</td>
    <td align="right">11.57</td>
    <td align="right">14.80</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.76</td>
    <td align="right">1.99</td>
    <td align="right">5.06</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.26</td>
    <td align="right">1.74</td>
    <td align="right">1.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.63</td>
    <td align="right">11.79</td>
    <td align="right">20.28</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">2.66</td>
    <td align="right">2.71</td>
    <td align="right">2.39</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.76</td>
    <td align="right">2.42</td>
    <td align="right">2.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">23.35</td>
    <td align="right">15.47</td>
    <td align="right">13.57</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.96</td>
    <td align="right">2.25</td>
    <td align="right">2.60</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.66</td>
    <td align="right">1.88</td>
    <td align="right">1.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">8.15</td>
    <td align="right">5.17</td>
    <td align="right">13.19</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">1.48</td>
    <td align="right">1.39</td>
    <td align="right">1.58</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">1.77</td>
    <td align="right">1.40</td>
    <td align="right">1.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">18.01</td>
    <td align="right">6.71</td>
    <td align="right">14.14</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">1.72</td>
    <td align="right">2.11</td>
    <td align="right">2.21</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">1.96</td>
    <td align="right">1.64</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">15.14</td>
    <td align="right">9.82</td>
    <td align="right">12.69</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">1.92</td>
    <td align="right">2.58</td>
    <td align="right">2.08</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">2.02</td>
    <td align="right">1.83</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">19.59</td>
    <td align="right">10.97</td>
    <td align="right">12.68</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">2.39</td>
    <td align="right">2.11</td>
    <td align="right">3.00</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">2.03</td>
    <td align="right">2.47</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.28</td>
    <td align="right">1.95</td>
    <td align="right">2.20</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.59</td>
    <td align="right">1.94</td>
    <td align="right">2.25</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.34</td>
    <td align="right">2.06</td>
    <td align="right">1.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.51</td>
    <td align="right">2.33</td>
    <td align="right">2.37</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.15</td>
    <td align="right">2.57</td>
    <td align="right">2.56</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.78</td>
    <td align="right">1.62</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.36</td>
    <td align="right">3.38</td>
    <td align="right">3.30</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.15</td>
    <td align="right">3.91</td>
    <td align="right">4.54</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.19</td>
    <td align="right">3.53</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.03</td>
    <td align="right">4.44</td>
    <td align="right">4.96</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.61</td>
    <td align="right">6.41</td>
    <td align="right">8.66</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.41</td>
    <td align="right">4.82</td>
    <td align="right">2.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.84</td>
    <td align="right">2.66</td>
    <td align="right">3.20</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">3.03</td>
    <td align="right">3.00</td>
    <td align="right">2.17</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.97</td>
    <td align="right">2.52</td>
    <td align="right">2.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">3.46</td>
    <td align="right">2.80</td>
    <td align="right">3.19</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.85</td>
    <td align="right">3.29</td>
    <td align="right">3.95</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">1.82</td>
    <td align="right">1.96</td>
    <td align="right">2.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.24</td>
    <td align="right">3.20</td>
    <td align="right">4.00</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">5.84</td>
    <td align="right">4.65</td>
    <td align="right">4.55</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">4.65</td>
    <td align="right">3.38</td>
    <td align="right">2.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">7.45</td>
    <td align="right">4.61</td>
    <td align="right">6.31</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">5.71</td>
    <td align="right">4.88</td>
    <td align="right">4.80</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">3.22</td>
    <td align="right">3.56</td>
    <td align="right">1.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.23</td>
    <td align="right">1.95</td>
    <td align="right">1.96</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.52</td>
    <td align="right">1.98</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.56</td>
    <td align="right">2.02</td>
    <td align="right">2.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.24</td>
    <td align="right">1.81</td>
    <td align="right">1.77</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.48</td>
    <td align="right">2.41</td>
    <td align="right">2.44</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.16</td>
    <td align="right">2.65</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.29</td>
    <td align="right">2.60</td>
    <td align="right">1.95</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.00</td>
    <td align="right">5.48</td>
    <td align="right">4.33</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.27</td>
    <td align="right">4.14</td>
    <td align="right">4.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.80</td>
    <td align="right">3.52</td>
    <td align="right">1.99</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.34</td>
    <td align="right">4.39</td>
    <td align="right">4.33</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.28</td>
    <td align="right">4.53</td>
    <td align="right">4.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">3.65</td>
    <td align="right">1.90</td>
    <td align="right">2.02</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.63</td>
    <td align="right">2.00</td>
    <td align="right">2.18</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.53</td>
    <td align="right">2.04</td>
    <td align="right">1.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">2.56</td>
    <td align="right">2.53</td>
    <td align="right">3.46</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.89</td>
    <td align="right">3.04</td>
    <td align="right">2.33</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.69</td>
    <td align="right">2.83</td>
    <td align="right">3.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.10</td>
    <td align="right">4.27</td>
    <td align="right">4.03</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.75</td>
    <td align="right">4.84</td>
    <td align="right">3.64</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">7.12</td>
    <td align="right">5.16</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">4.43</td>
    <td align="right">5.16</td>
    <td align="right">2.89</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">6.91</td>
    <td align="right">5.17</td>
    <td align="right">4.84</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">5.50</td>
    <td align="right">5.51</td>
    <td align="right">5.25</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.64</td>
    <td align="right">15.59</td>
    <td align="right">10.03</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.51</td>
    <td align="right">11.22</td>
    <td align="right">20.97</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.18</td>
    <td align="right">3.73</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.04</td>
    <td align="right">4.05</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">44.75</td>
    <td align="right">37.93</td>
    <td align="right">31.28</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.20</td>
    <td align="right">8.63</td>
    <td align="right">9.76</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.18</td>
    <td align="right">11.04</td>
    <td align="right">9.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">68.12</td>
    <td align="right">52.10</td>
    <td align="right">29.36</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.12</td>
    <td align="right">12.89</td>
    <td align="right">10.82</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.44</td>
    <td align="right">12.65</td>
    <td align="right">10.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">94.22</td>
    <td align="right">69.07</td>
    <td align="right">33.21</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.02</td>
    <td align="right">13.40</td>
    <td align="right">12.96</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.73</td>
    <td align="right">11.88</td>
    <td align="right">11.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">12.80</td>
    <td align="right">13.35</td>
    <td align="right">23.83</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.53</td>
    <td align="right">4.21</td>
    <td align="right">5.00</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">4.13</td>
    <td align="right">4.88</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">31.69</td>
    <td align="right">30.81</td>
    <td align="right">30.52</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">9.77</td>
    <td align="right">9.69</td>
    <td align="right">9.69</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">9.81</td>
    <td align="right">8.62</td>
    <td align="right">7.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">57.84</td>
    <td align="right">34.01</td>
    <td align="right">21.12</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">7.32</td>
    <td align="right">8.07</td>
    <td align="right">7.29</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">7.09</td>
    <td align="right">7.72</td>
    <td align="right">7.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">60.31</td>
    <td align="right">46.95</td>
    <td align="right">24.22</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">10.30</td>
    <td align="right">8.97</td>
    <td align="right">10.32</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">9.20</td>
    <td align="right">6.94</td>
    <td align="right">8.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.23</td>
    <td align="right">3.14</td>
    <td align="right">3.49</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.04</td>
    <td align="right">3.03</td>
    <td align="right">3.12</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.65</td>
    <td align="right">3.54</td>
    <td align="right">3.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.48</td>
    <td align="right">6.10</td>
    <td align="right">6.40</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.15</td>
    <td align="right">6.00</td>
    <td align="right">6.58</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.74</td>
    <td align="right">4.98</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.55</td>
    <td align="right">11.31</td>
    <td align="right">13.30</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">15.42</td>
    <td align="right">16.74</td>
    <td align="right">14.92</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">11.64</td>
    <td align="right">11.50</td>
    <td align="right">9.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.47</td>
    <td align="right">16.88</td>
    <td align="right">18.54</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.95</td>
    <td align="right">17.43</td>
    <td align="right">20.23</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">14.30</td>
    <td align="right">13.16</td>
    <td align="right">7.15</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">3.12</td>
    <td align="right">2.98</td>
    <td align="right">2.96</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">3.21</td>
    <td align="right">2.95</td>
    <td align="right">2.97</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">2.61</td>
    <td align="right">2.90</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">4.63</td>
    <td align="right">5.56</td>
    <td align="right">6.58</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">5.74</td>
    <td align="right">8.09</td>
    <td align="right">6.17</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.10</td>
    <td align="right">4.04</td>
    <td align="right">4.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">11.19</td>
    <td align="right">10.30</td>
    <td align="right">10.72</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">11.19</td>
    <td align="right">11.01</td>
    <td align="right">12.68</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">8.62</td>
    <td align="right">8.81</td>
    <td align="right">7.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">17.07</td>
    <td align="right">17.28</td>
    <td align="right">15.98</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">16.49</td>
    <td align="right">14.91</td>
    <td align="right">16.17</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">10.23</td>
    <td align="right">11.62</td>
    <td align="right">7.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.76</td>
    <td align="right">3.17</td>
    <td align="right">3.05</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.09</td>
    <td align="right">3.29</td>
    <td align="right">3.32</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.99</td>
    <td align="right">3.01</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.32</td>
    <td align="right">3.65</td>
    <td align="right">3.62</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.52</td>
    <td align="right">6.27</td>
    <td align="right">5.60</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.18</td>
    <td align="right">5.84</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">9.12</td>
    <td align="right">8.95</td>
    <td align="right">6.78</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.21</td>
    <td align="right">10.77</td>
    <td align="right">10.71</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.11</td>
    <td align="right">9.86</td>
    <td align="right">11.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.88</td>
    <td align="right">11.45</td>
    <td align="right">6.74</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.82</td>
    <td align="right">15.20</td>
    <td align="right">16.06</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.85</td>
    <td align="right">16.71</td>
    <td align="right">15.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">2.80</td>
    <td align="right">3.34</td>
    <td align="right">3.38</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">2.94</td>
    <td align="right">2.85</td>
    <td align="right">2.87</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.97</td>
    <td align="right">2.91</td>
    <td align="right">3.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.12</td>
    <td align="right">3.26</td>
    <td align="right">3.31</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">5.11</td>
    <td align="right">4.90</td>
    <td align="right">4.77</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.60</td>
    <td align="right">5.42</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">8.42</td>
    <td align="right">8.32</td>
    <td align="right">5.76</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">11.16</td>
    <td align="right">10.08</td>
    <td align="right">10.85</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">11.10</td>
    <td align="right">10.69</td>
    <td align="right">11.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">11.02</td>
    <td align="right">12.17</td>
    <td align="right">8.00</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">16.56</td>
    <td align="right">16.41</td>
    <td align="right">16.44</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">16.69</td>
    <td align="right">17.11</td>
    <td align="right">20.14</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">36.04</td>
    <td align="right">5.77</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.06</td>
    <td align="right">12.49</td>
    <td align="right">16.91</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.84</td>
    <td align="right">4.22</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.96</td>
    <td align="right">5.21</td>
    <td align="right">5.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.48</td>
    <td align="right">17.81</td>
    <td align="right">17.52</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.93</td>
    <td align="right">4.76</td>
    <td align="right">4.95</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.03</td>
    <td align="right">5.89</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.54</td>
    <td align="right">21.31</td>
    <td align="right">16.59</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.62</td>
    <td align="right">5.41</td>
    <td align="right">5.36</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.35</td>
    <td align="right">6.59</td>
    <td align="right">6.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.12</td>
    <td align="right">27.75</td>
    <td align="right">17.35</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">10.28</td>
    <td align="right">6.05</td>
    <td align="right">5.99</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.48</td>
    <td align="right">7.35</td>
    <td align="right">7.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">13.47</td>
    <td align="right">13.66</td>
    <td align="right">18.01</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">6.06</td>
    <td align="right">4.38</td>
    <td align="right">4.36</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">7.15</td>
    <td align="right">5.58</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">20.93</td>
    <td align="right">19.43</td>
    <td align="right">18.64</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">7.19</td>
    <td align="right">4.89</td>
    <td align="right">4.90</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">8.37</td>
    <td align="right">6.11</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">26.45</td>
    <td align="right">24.06</td>
    <td align="right">17.78</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">8.93</td>
    <td align="right">5.50</td>
    <td align="right">5.49</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">9.72</td>
    <td align="right">6.89</td>
    <td align="right">6.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">34.68</td>
    <td align="right">30.65</td>
    <td align="right">18.18</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">10.09</td>
    <td align="right">6.09</td>
    <td align="right">6.11</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">10.94</td>
    <td align="right">7.57</td>
    <td align="right">7.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.85</td>
    <td align="right">5.57</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.17</td>
    <td align="right">5.57</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.42</td>
    <td align="right">3.94</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.75</td>
    <td align="right">8.43</td>
    <td align="right">8.49</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.42</td>
    <td align="right">8.67</td>
    <td align="right">8.68</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.90</td>
    <td align="right">4.83</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.55</td>
    <td align="right">10.92</td>
    <td align="right">10.93</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.90</td>
    <td align="right">10.51</td>
    <td align="right">10.46</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.94</td>
    <td align="right">7.00</td>
    <td align="right">5.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.33</td>
    <td align="right">13.94</td>
    <td align="right">13.81</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.02</td>
    <td align="right">13.68</td>
    <td align="right">12.97</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.07</td>
    <td align="right">7.04</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.97</td>
    <td align="right">5.72</td>
    <td align="right">5.74</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">9.16</td>
    <td align="right">5.47</td>
    <td align="right">5.45</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.45</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">11.19</td>
    <td align="right">8.69</td>
    <td align="right">8.67</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">19.31</td>
    <td align="right">8.76</td>
    <td align="right">7.90</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.96</td>
    <td align="right">4.94</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">15.53</td>
    <td align="right">11.12</td>
    <td align="right">11.41</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.22</td>
    <td align="right">10.68</td>
    <td align="right">10.73</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.19</td>
    <td align="right">7.15</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">17.24</td>
    <td align="right">14.39</td>
    <td align="right">14.37</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">19.01</td>
    <td align="right">13.82</td>
    <td align="right">13.66</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.23</td>
    <td align="right">7.17</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.30</td>
    <td align="right">3.82</td>
    <td align="right">3.88</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.50</td>
    <td align="right">5.53</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.65</td>
    <td align="right">5.46</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.31</td>
    <td align="right">5.53</td>
    <td align="right">4.67</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.80</td>
    <td align="right">5.80</td>
    <td align="right">5.07</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.94</td>
    <td align="right">6.98</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.06</td>
    <td align="right">6.92</td>
    <td align="right">5.14</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.78</td>
    <td align="right">9.34</td>
    <td align="right">7.61</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.90</td>
    <td align="right">9.29</td>
    <td align="right">7.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.16</td>
    <td align="right">7.13</td>
    <td align="right">5.06</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.23</td>
    <td align="right">10.66</td>
    <td align="right">7.68</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.25</td>
    <td align="right">10.44</td>
    <td align="right">7.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">3.29</td>
    <td align="right">3.90</td>
    <td align="right">3.92</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.51</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.64</td>
    <td align="right">5.38</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.34</td>
    <td align="right">5.56</td>
    <td align="right">4.70</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">4.87</td>
    <td align="right">6.09</td>
    <td align="right">5.21</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">7.14</td>
    <td align="right">7.27</td>
    <td align="right">6.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.14</td>
    <td align="right">7.01</td>
    <td align="right">5.23</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">9.79</td>
    <td align="right">9.67</td>
    <td align="right">7.85</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">9.90</td>
    <td align="right">9.26</td>
    <td align="right">7.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.21</td>
    <td align="right">7.12</td>
    <td align="right">5.29</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">10.25</td>
    <td align="right">10.69</td>
    <td align="right">7.74</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">10.45</td>
    <td align="right">10.52</td>
    <td align="right">7.61</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">44.74</td>
    <td align="right">21.99</td>
    <td align="right">9.51</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.77</td>
    <td align="right">13.23</td>
    <td align="right">17.68</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.06</td>
    <td align="right">4.55</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.90</td>
    <td align="right">5.57</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">24.58</td>
    <td align="right">20.87</td>
    <td align="right">18.73</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.71</td>
    <td align="right">5.52</td>
    <td align="right">7.24</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.04</td>
    <td align="right">6.82</td>
    <td align="right">7.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">44.19</td>
    <td align="right">42.79</td>
    <td align="right">21.04</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.53</td>
    <td align="right">12.11</td>
    <td align="right">12.52</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">15.22</td>
    <td align="right">10.96</td>
    <td align="right">12.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">74.74</td>
    <td align="right">82.52</td>
    <td align="right">24.24</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.60</td>
    <td align="right">16.72</td>
    <td align="right">14.97</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">21.34</td>
    <td align="right">21.19</td>
    <td align="right">20.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">15.82</td>
    <td align="right">14.50</td>
    <td align="right">19.06</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">7.54</td>
    <td align="right">4.68</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">8.71</td>
    <td align="right">5.96</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">25.97</td>
    <td align="right">21.41</td>
    <td align="right">20.44</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">9.36</td>
    <td align="right">5.47</td>
    <td align="right">5.41</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">10.63</td>
    <td align="right">7.20</td>
    <td align="right">6.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">40.41</td>
    <td align="right">46.04</td>
    <td align="right">20.74</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">13.03</td>
    <td align="right">8.23</td>
    <td align="right">8.47</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">14.23</td>
    <td align="right">9.00</td>
    <td align="right">14.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">76.64</td>
    <td align="right">78.28</td>
    <td align="right">25.35</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">20.60</td>
    <td align="right">14.35</td>
    <td align="right">14.24</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">21.28</td>
    <td align="right">17.92</td>
    <td align="right">19.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.32</td>
    <td align="right">6.28</td>
    <td align="right">6.30</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.58</td>
    <td align="right">6.31</td>
    <td align="right">6.34</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.72</td>
    <td align="right">4.23</td>
    <td align="right">4.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.50</td>
    <td align="right">10.91</td>
    <td align="right">10.50</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">21.47</td>
    <td align="right">10.36</td>
    <td align="right">9.66</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.61</td>
    <td align="right">5.47</td>
    <td align="right">4.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">21.61</td>
    <td align="right">17.71</td>
    <td align="right">13.69</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">22.92</td>
    <td align="right">14.39</td>
    <td align="right">13.90</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.59</td>
    <td align="right">12.30</td>
    <td align="right">9.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">29.30</td>
    <td align="right">27.43</td>
    <td align="right">27.00</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">34.63</td>
    <td align="right">29.34</td>
    <td align="right">21.84</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">13.92</td>
    <td align="right">19.20</td>
    <td align="right">15.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">9.55</td>
    <td align="right">6.44</td>
    <td align="right">6.38</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">9.49</td>
    <td align="right">5.94</td>
    <td align="right">5.79</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.79</td>
    <td align="right">4.33</td>
    <td align="right">4.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">21.48</td>
    <td align="right">10.49</td>
    <td align="right">10.33</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">21.84</td>
    <td align="right">10.07</td>
    <td align="right">8.96</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.50</td>
    <td align="right">6.30</td>
    <td align="right">4.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">22.13</td>
    <td align="right">14.65</td>
    <td align="right">18.53</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">22.38</td>
    <td align="right">14.98</td>
    <td align="right">15.43</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">8.23</td>
    <td align="right">10.36</td>
    <td align="right">8.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">35.56</td>
    <td align="right">33.26</td>
    <td align="right">28.38</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">34.90</td>
    <td align="right">25.99</td>
    <td align="right">25.23</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">12.24</td>
    <td align="right">16.66</td>
    <td align="right">13.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.75</td>
    <td align="right">4.19</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.97</td>
    <td align="right">6.03</td>
    <td align="right">6.06</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.09</td>
    <td align="right">5.87</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">4.05</td>
    <td align="right">6.46</td>
    <td align="right">5.35</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.39</td>
    <td align="right">6.46</td>
    <td align="right">5.58</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.14</td>
    <td align="right">8.05</td>
    <td align="right">6.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.05</td>
    <td align="right">10.15</td>
    <td align="right">7.16</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.27</td>
    <td align="right">11.67</td>
    <td align="right">9.27</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">14.36</td>
    <td align="right">12.80</td>
    <td align="right">10.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">13.16</td>
    <td align="right">17.98</td>
    <td align="right">14.14</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">17.50</td>
    <td align="right">18.78</td>
    <td align="right">15.61</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">18.40</td>
    <td align="right">18.29</td>
    <td align="right">13.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.66</td>
    <td align="right">4.23</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">5.13</td>
    <td align="right">5.98</td>
    <td align="right">5.95</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.06</td>
    <td align="right">5.91</td>
    <td align="right">5.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">4.07</td>
    <td align="right">6.18</td>
    <td align="right">5.16</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">5.55</td>
    <td align="right">6.69</td>
    <td align="right">5.99</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">7.98</td>
    <td align="right">8.40</td>
    <td align="right">7.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">12.28</td>
    <td align="right">13.53</td>
    <td align="right">9.74</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">12.46</td>
    <td align="right">12.00</td>
    <td align="right">10.28</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">14.36</td>
    <td align="right">10.72</td>
    <td align="right">8.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">12.79</td>
    <td align="right">17.93</td>
    <td align="right">11.92</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.83</td>
    <td align="right">18.57</td>
    <td align="right">13.44</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">16.74</td>
    <td align="right">19.52</td>
    <td align="right">14.02</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.17</td>
    <td align="right">35.40</td>
    <td align="right">18.13</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.09</td>
    <td align="right">41.65</td>
    <td align="right">36.35</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.59</td>
    <td align="right">16.01</td>
    <td align="right">15.92</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.07</td>
    <td align="right">19.69</td>
    <td align="right">19.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.15</td>
    <td align="right">64.38</td>
    <td align="right">39.31</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.25</td>
    <td align="right">19.36</td>
    <td align="right">19.23</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.09</td>
    <td align="right">18.67</td>
    <td align="right">18.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.47</td>
    <td align="right">77.69</td>
    <td align="right">38.34</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.14</td>
    <td align="right">18.42</td>
    <td align="right">18.45</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.99</td>
    <td align="right">18.24</td>
    <td align="right">18.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.92</td>
    <td align="right">96.50</td>
    <td align="right">37.41</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.21</td>
    <td align="right">18.75</td>
    <td align="right">18.76</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.89</td>
    <td align="right">19.96</td>
    <td align="right">19.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">27.98</td>
    <td align="right">40.01</td>
    <td align="right">37.06</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">12.24</td>
    <td align="right">15.42</td>
    <td align="right">15.43</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">13.72</td>
    <td align="right">16.16</td>
    <td align="right">16.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">42.55</td>
    <td align="right">59.05</td>
    <td align="right">39.43</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">14.46</td>
    <td align="right">17.06</td>
    <td align="right">17.18</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">15.04</td>
    <td align="right">17.22</td>
    <td align="right">17.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">51.12</td>
    <td align="right">73.74</td>
    <td align="right">38.61</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.70</td>
    <td align="right">17.62</td>
    <td align="right">17.61</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">16.57</td>
    <td align="right">17.46</td>
    <td align="right">17.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">64.93</td>
    <td align="right">98.57</td>
    <td align="right">41.44</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">16.39</td>
    <td align="right">17.67</td>
    <td align="right">18.33</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">15.91</td>
    <td align="right">19.15</td>
    <td align="right">19.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.25</td>
    <td align="right">20.49</td>
    <td align="right">20.49</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.53</td>
    <td align="right">22.14</td>
    <td align="right">22.14</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.55</td>
    <td align="right">13.57</td>
    <td align="right">13.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.26</td>
    <td align="right">26.71</td>
    <td align="right">26.71</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.47</td>
    <td align="right">28.94</td>
    <td align="right">29.00</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.78</td>
    <td align="right">16.49</td>
    <td align="right">15.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.87</td>
    <td align="right">32.96</td>
    <td align="right">32.95</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.56</td>
    <td align="right">45.56</td>
    <td align="right">45.71</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.52</td>
    <td align="right">19.57</td>
    <td align="right">19.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.39</td>
    <td align="right">35.81</td>
    <td align="right">35.89</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.52</td>
    <td align="right">55.28</td>
    <td align="right">55.34</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.57</td>
    <td align="right">24.67</td>
    <td align="right">24.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">17.25</td>
    <td align="right">20.63</td>
    <td align="right">20.55</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.37</td>
    <td align="right">20.78</td>
    <td align="right">20.78</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">11.36</td>
    <td align="right">14.25</td>
    <td align="right">14.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.31</td>
    <td align="right">26.53</td>
    <td align="right">26.55</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.48</td>
    <td align="right">27.69</td>
    <td align="right">27.71</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">13.65</td>
    <td align="right">18.10</td>
    <td align="right">18.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.15</td>
    <td align="right">34.52</td>
    <td align="right">33.92</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">65.56</td>
    <td align="right">46.05</td>
    <td align="right">46.03</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">16.23</td>
    <td align="right">19.87</td>
    <td align="right">19.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">34.86</td>
    <td align="right">36.58</td>
    <td align="right">36.50</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.24</td>
    <td align="right">55.12</td>
    <td align="right">55.05</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">25.36</td>
    <td align="right">25.38</td>
    <td align="right">25.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">14.65</td>
    <td align="right">16.02</td>
    <td align="right">15.59</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.15</td>
    <td align="right">20.53</td>
    <td align="right">20.47</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.55</td>
    <td align="right">22.13</td>
    <td align="right">22.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">18.99</td>
    <td align="right">20.10</td>
    <td align="right">20.14</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.33</td>
    <td align="right">26.71</td>
    <td align="right">26.75</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.40</td>
    <td align="right">28.92</td>
    <td align="right">28.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.43</td>
    <td align="right">24.84</td>
    <td align="right">24.78</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.84</td>
    <td align="right">33.18</td>
    <td align="right">33.24</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.80</td>
    <td align="right">45.67</td>
    <td align="right">45.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">33.81</td>
    <td align="right">34.91</td>
    <td align="right">34.84</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.44</td>
    <td align="right">36.03</td>
    <td align="right">36.02</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.54</td>
    <td align="right">55.29</td>
    <td align="right">55.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4960</td>
    <td align="right">14.91</td>
    <td align="right">15.98</td>
    <td align="right">16.02</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">17.33</td>
    <td align="right">20.63</td>
    <td align="right">20.65</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.39</td>
    <td align="right">20.68</td>
    <td align="right">20.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">20.33</td>
    <td align="right">20.16</td>
    <td align="right">20.19</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.25</td>
    <td align="right">26.59</td>
    <td align="right">26.58</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.45</td>
    <td align="right">27.68</td>
    <td align="right">27.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">28.24</td>
    <td align="right">23.29</td>
    <td align="right">23.17</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.04</td>
    <td align="right">34.75</td>
    <td align="right">34.18</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">65.65</td>
    <td align="right">46.10</td>
    <td align="right">46.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">34.40</td>
    <td align="right">34.76</td>
    <td align="right">34.74</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">34.82</td>
    <td align="right">36.56</td>
    <td align="right">36.71</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.48</td>
    <td align="right">55.16</td>
    <td align="right">55.25</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">81.16</td>
    <td align="right">110.01</td>
    <td align="right">21.42</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.52</td>
    <td align="right">42.89</td>
    <td align="right">39.22</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.26</td>
    <td align="right">16.14</td>
    <td align="right">16.16</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.32</td>
    <td align="right">20.05</td>
    <td align="right">20.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">37.95</td>
    <td align="right">65.30</td>
    <td align="right">42.14</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">20.20</td>
    <td align="right">25.74</td>
    <td align="right">24.18</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">18.14</td>
    <td align="right">22.04</td>
    <td align="right">24.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">87.93</td>
    <td align="right">100.35</td>
    <td align="right">48.09</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">26.71</td>
    <td align="right">31.06</td>
    <td align="right">24.37</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">32.17</td>
    <td align="right">26.83</td>
    <td align="right">30.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">133.13</td>
    <td align="right">167.73</td>
    <td align="right">56.70</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">41.49</td>
    <td align="right">30.95</td>
    <td align="right">33.34</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">38.71</td>
    <td align="right">39.65</td>
    <td align="right">47.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">32.95</td>
    <td align="right">49.04</td>
    <td align="right">49.00</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">18.75</td>
    <td align="right">21.83</td>
    <td align="right">22.44</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.36</td>
    <td align="right">27.16</td>
    <td align="right">28.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">93.87</td>
    <td align="right">140.95</td>
    <td align="right">80.62</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">23.89</td>
    <td align="right">19.81</td>
    <td align="right">19.89</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">18.19</td>
    <td align="right">20.53</td>
    <td align="right">19.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">88.44</td>
    <td align="right">207.92</td>
    <td align="right">72.77</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">38.89</td>
    <td align="right">47.17</td>
    <td align="right">41.57</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">52.77</td>
    <td align="right">52.18</td>
    <td align="right">53.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">265.69</td>
    <td align="right">329.59</td>
    <td align="right">96.90</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">47.87</td>
    <td align="right">43.68</td>
    <td align="right">52.99</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">53.67</td>
    <td align="right">48.99</td>
    <td align="right">47.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">19.43</td>
    <td align="right">33.39</td>
    <td align="right">35.75</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">63.51</td>
    <td align="right">24.57</td>
    <td align="right">23.53</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.85</td>
    <td align="right">13.86</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">24.46</td>
    <td align="right">32.44</td>
    <td align="right">37.37</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">68.79</td>
    <td align="right">37.74</td>
    <td align="right">37.74</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">13.11</td>
    <td align="right">19.77</td>
    <td align="right">18.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">38.86</td>
    <td align="right">50.44</td>
    <td align="right">47.72</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">74.94</td>
    <td align="right">58.52</td>
    <td align="right">56.84</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">20.91</td>
    <td align="right">27.14</td>
    <td align="right">30.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">69.43</td>
    <td align="right">73.70</td>
    <td align="right">66.46</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">98.93</td>
    <td align="right">75.73</td>
    <td align="right">78.21</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">43.81</td>
    <td align="right">49.84</td>
    <td align="right">45.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.33</td>
    <td align="right">21.77</td>
    <td align="right">21.97</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">33.90</td>
    <td align="right">22.37</td>
    <td align="right">22.59</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">11.87</td>
    <td align="right">14.90</td>
    <td align="right">14.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">24.30</td>
    <td align="right">29.75</td>
    <td align="right">29.26</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">65.58</td>
    <td align="right">33.53</td>
    <td align="right">32.90</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">14.61</td>
    <td align="right">19.94</td>
    <td align="right">19.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">40.26</td>
    <td align="right">52.31</td>
    <td align="right">52.00</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">74.70</td>
    <td align="right">50.07</td>
    <td align="right">50.50</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">28.47</td>
    <td align="right">31.72</td>
    <td align="right">22.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">42.79</td>
    <td align="right">56.92</td>
    <td align="right">56.55</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">104.73</td>
    <td align="right">76.32</td>
    <td align="right">81.11</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">46.14</td>
    <td align="right">79.07</td>
    <td align="right">70.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.98</td>
    <td align="right">16.98</td>
    <td align="right">16.34</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.41</td>
    <td align="right">21.35</td>
    <td align="right">21.77</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">36.42</td>
    <td align="right">23.54</td>
    <td align="right">23.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">22.77</td>
    <td align="right">24.56</td>
    <td align="right">23.30</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">24.67</td>
    <td align="right">31.24</td>
    <td align="right">29.73</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">78.52</td>
    <td align="right">48.48</td>
    <td align="right">43.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">47.98</td>
    <td align="right">38.23</td>
    <td align="right">41.10</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">39.14</td>
    <td align="right">46.69</td>
    <td align="right">46.32</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">72.88</td>
    <td align="right">55.03</td>
    <td align="right">54.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">75.08</td>
    <td align="right">82.64</td>
    <td align="right">82.33</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">52.31</td>
    <td align="right">65.43</td>
    <td align="right">66.10</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">100.95</td>
    <td align="right">79.57</td>
    <td align="right">85.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">16.09</td>
    <td align="right">16.72</td>
    <td align="right">17.12</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.27</td>
    <td align="right">22.43</td>
    <td align="right">22.09</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">31.62</td>
    <td align="right">21.90</td>
    <td align="right">22.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">27.23</td>
    <td align="right">26.81</td>
    <td align="right">23.90</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">22.53</td>
    <td align="right">27.97</td>
    <td align="right">27.63</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">48.81</td>
    <td align="right">32.30</td>
    <td align="right">33.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">42.72</td>
    <td align="right">32.30</td>
    <td align="right">33.02</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">40.40</td>
    <td align="right">49.47</td>
    <td align="right">55.49</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">80.12</td>
    <td align="right">56.28</td>
    <td align="right">58.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">75.32</td>
    <td align="right">87.28</td>
    <td align="right">80.06</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">56.64</td>
    <td align="right">72.67</td>
    <td align="right">81.43</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">110.98</td>
    <td align="right">80.13</td>
    <td align="right">78.01</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.60</td>
    <td align="right">10.47</td>
    <td align="right">7.24</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.79</td>
    <td align="right">22.87</td>
    <td align="right">26.62</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.58</td>
    <td align="right">12.40</td>
    <td align="right">12.38</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.71</td>
    <td align="right">13.87</td>
    <td align="right">13.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.53</td>
    <td align="right">35.60</td>
    <td align="right">28.82</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.09</td>
    <td align="right">14.07</td>
    <td align="right">14.09</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.47</td>
    <td align="right">15.10</td>
    <td align="right">15.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.95</td>
    <td align="right">47.45</td>
    <td align="right">29.89</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.67</td>
    <td align="right">15.39</td>
    <td align="right">15.38</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.62</td>
    <td align="right">16.73</td>
    <td align="right">16.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.18</td>
    <td align="right">60.37</td>
    <td align="right">30.92</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.60</td>
    <td align="right">16.21</td>
    <td align="right">16.29</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.92</td>
    <td align="right">17.85</td>
    <td align="right">17.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">19.17</td>
    <td align="right">27.93</td>
    <td align="right">28.11</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">9.58</td>
    <td align="right">12.38</td>
    <td align="right">12.38</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">12.57</td>
    <td align="right">14.66</td>
    <td align="right">14.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">27.99</td>
    <td align="right">40.93</td>
    <td align="right">30.80</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">13.09</td>
    <td align="right">14.96</td>
    <td align="right">14.90</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">14.38</td>
    <td align="right">15.85</td>
    <td align="right">15.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">33.55</td>
    <td align="right">53.34</td>
    <td align="right">29.44</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.53</td>
    <td align="right">16.06</td>
    <td align="right">16.20</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">15.29</td>
    <td align="right">17.26</td>
    <td align="right">17.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">47.98</td>
    <td align="right">67.43</td>
    <td align="right">31.65</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">15.44</td>
    <td align="right">17.27</td>
    <td align="right">17.00</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">16.71</td>
    <td align="right">18.63</td>
    <td align="right">19.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.65</td>
    <td align="right">16.08</td>
    <td align="right">16.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.03</td>
    <td align="right">16.61</td>
    <td align="right">16.66</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.01</td>
    <td align="right">8.99</td>
    <td align="right">9.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.31</td>
    <td align="right">22.49</td>
    <td align="right">22.13</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.92</td>
    <td align="right">22.36</td>
    <td align="right">22.38</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.98</td>
    <td align="right">13.94</td>
    <td align="right">13.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.14</td>
    <td align="right">32.02</td>
    <td align="right">32.04</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.61</td>
    <td align="right">30.53</td>
    <td align="right">30.60</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.50</td>
    <td align="right">17.54</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.87</td>
    <td align="right">35.58</td>
    <td align="right">35.60</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.88</td>
    <td align="right">35.76</td>
    <td align="right">35.72</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.23</td>
    <td align="right">20.51</td>
    <td align="right">20.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">13.19</td>
    <td align="right">16.86</td>
    <td align="right">16.91</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.16</td>
    <td align="right">16.35</td>
    <td align="right">16.35</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">7.05</td>
    <td align="right">9.30</td>
    <td align="right">9.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">17.91</td>
    <td align="right">25.43</td>
    <td align="right">25.40</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">19.47</td>
    <td align="right">23.69</td>
    <td align="right">23.77</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">10.54</td>
    <td align="right">13.41</td>
    <td align="right">13.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">24.84</td>
    <td align="right">32.12</td>
    <td align="right">31.58</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.64</td>
    <td align="right">31.05</td>
    <td align="right">30.32</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">13.16</td>
    <td align="right">17.85</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.33</td>
    <td align="right">35.80</td>
    <td align="right">35.35</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">33.89</td>
    <td align="right">37.64</td>
    <td align="right">38.18</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">17.43</td>
    <td align="right">20.78</td>
    <td align="right">20.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.55</td>
    <td align="right">9.32</td>
    <td align="right">9.35</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.62</td>
    <td align="right">15.88</td>
    <td align="right">16.07</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.19</td>
    <td align="right">16.67</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.88</td>
    <td align="right">13.67</td>
    <td align="right">13.65</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.03</td>
    <td align="right">22.30</td>
    <td align="right">21.60</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.08</td>
    <td align="right">22.34</td>
    <td align="right">22.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.36</td>
    <td align="right">17.62</td>
    <td align="right">17.58</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.61</td>
    <td align="right">31.92</td>
    <td align="right">31.96</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.52</td>
    <td align="right">30.45</td>
    <td align="right">30.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">15.54</td>
    <td align="right">20.57</td>
    <td align="right">20.38</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.87</td>
    <td align="right">35.54</td>
    <td align="right">35.57</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">31.89</td>
    <td align="right">35.67</td>
    <td align="right">35.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4960</td>
    <td align="right">6.56</td>
    <td align="right">9.31</td>
    <td align="right">9.45</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">13.08</td>
    <td align="right">16.88</td>
    <td align="right">16.84</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.15</td>
    <td align="right">15.69</td>
    <td align="right">16.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">10.89</td>
    <td align="right">13.05</td>
    <td align="right">13.73</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">18.05</td>
    <td align="right">25.44</td>
    <td align="right">25.00</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">19.27</td>
    <td align="right">23.37</td>
    <td align="right">23.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">14.25</td>
    <td align="right">17.46</td>
    <td align="right">17.46</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">24.84</td>
    <td align="right">32.30</td>
    <td align="right">32.19</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">26.90</td>
    <td align="right">31.05</td>
    <td align="right">30.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">17.64</td>
    <td align="right">20.37</td>
    <td align="right">20.63</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.69</td>
    <td align="right">35.67</td>
    <td align="right">35.78</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">33.82</td>
    <td align="right">38.04</td>
    <td align="right">38.17</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">73.91</td>
    <td align="right">42.23</td>
    <td align="right">10.09</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">13.93</td>
    <td align="right">22.54</td>
    <td align="right">27.95</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.63</td>
    <td align="right">12.50</td>
    <td align="right">12.46</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.78</td>
    <td align="right">13.89</td>
    <td align="right">13.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">18.92</td>
    <td align="right">34.08</td>
    <td align="right">28.98</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.73</td>
    <td align="right">13.61</td>
    <td align="right">13.67</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.19</td>
    <td align="right">14.80</td>
    <td align="right">14.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.80</td>
    <td align="right">52.50</td>
    <td align="right">30.03</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.60</td>
    <td align="right">14.89</td>
    <td align="right">14.77</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.04</td>
    <td align="right">16.14</td>
    <td align="right">16.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">30.80</td>
    <td align="right">60.14</td>
    <td align="right">30.36</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">14.33</td>
    <td align="right">15.75</td>
    <td align="right">15.65</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">15.43</td>
    <td align="right">19.19</td>
    <td align="right">17.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">19.41</td>
    <td align="right">27.70</td>
    <td align="right">30.02</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">9.61</td>
    <td align="right">12.46</td>
    <td align="right">12.49</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">12.64</td>
    <td align="right">14.47</td>
    <td align="right">14.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">27.10</td>
    <td align="right">40.52</td>
    <td align="right">31.15</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">12.62</td>
    <td align="right">14.55</td>
    <td align="right">14.54</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">14.17</td>
    <td align="right">15.27</td>
    <td align="right">15.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">33.35</td>
    <td align="right">51.57</td>
    <td align="right">29.94</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">14.34</td>
    <td align="right">15.64</td>
    <td align="right">15.48</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">14.74</td>
    <td align="right">16.61</td>
    <td align="right">16.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">48.14</td>
    <td align="right">68.21</td>
    <td align="right">31.91</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">15.60</td>
    <td align="right">17.49</td>
    <td align="right">17.37</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">16.65</td>
    <td align="right">18.71</td>
    <td align="right">18.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.64</td>
    <td align="right">16.65</td>
    <td align="right">16.65</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.34</td>
    <td align="right">17.42</td>
    <td align="right">17.39</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.19</td>
    <td align="right">9.30</td>
    <td align="right">9.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.59</td>
    <td align="right">21.21</td>
    <td align="right">21.18</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.84</td>
    <td align="right">21.45</td>
    <td align="right">21.31</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.12</td>
    <td align="right">13.43</td>
    <td align="right">13.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.64</td>
    <td align="right">31.95</td>
    <td align="right">32.19</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.17</td>
    <td align="right">30.38</td>
    <td align="right">30.42</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">12.94</td>
    <td align="right">16.65</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">26.34</td>
    <td align="right">35.59</td>
    <td align="right">35.44</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">32.73</td>
    <td align="right">35.10</td>
    <td align="right">35.08</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">15.29</td>
    <td align="right">19.61</td>
    <td align="right">19.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">13.47</td>
    <td align="right">16.90</td>
    <td align="right">16.88</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">14.36</td>
    <td align="right">16.10</td>
    <td align="right">16.00</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">7.15</td>
    <td align="right">9.25</td>
    <td align="right">8.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">17.12</td>
    <td align="right">23.63</td>
    <td align="right">23.60</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">21.08</td>
    <td align="right">22.09</td>
    <td align="right">22.22</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">11.74</td>
    <td align="right">12.94</td>
    <td align="right">12.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">24.76</td>
    <td align="right">32.76</td>
    <td align="right">32.46</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">27.45</td>
    <td align="right">31.10</td>
    <td align="right">30.81</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">12.87</td>
    <td align="right">17.14</td>
    <td align="right">17.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">29.21</td>
    <td align="right">37.08</td>
    <td align="right">37.06</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">35.01</td>
    <td align="right">38.05</td>
    <td align="right">38.46</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">18.10</td>
    <td align="right">21.74</td>
    <td align="right">21.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.71</td>
    <td align="right">9.51</td>
    <td align="right">9.53</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.61</td>
    <td align="right">16.57</td>
    <td align="right">16.59</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.29</td>
    <td align="right">17.42</td>
    <td align="right">17.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.70</td>
    <td align="right">13.33</td>
    <td align="right">13.28</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.67</td>
    <td align="right">21.43</td>
    <td align="right">21.57</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.04</td>
    <td align="right">21.66</td>
    <td align="right">21.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">12.59</td>
    <td align="right">16.78</td>
    <td align="right">16.89</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.87</td>
    <td align="right">32.42</td>
    <td align="right">32.41</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.54</td>
    <td align="right">30.76</td>
    <td align="right">30.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">16.92</td>
    <td align="right">21.59</td>
    <td align="right">21.72</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">27.57</td>
    <td align="right">37.29</td>
    <td align="right">37.08</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">34.29</td>
    <td align="right">36.49</td>
    <td align="right">36.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">6.88</td>
    <td align="right">9.65</td>
    <td align="right">9.62</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">13.65</td>
    <td align="right">17.11</td>
    <td align="right">17.15</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">14.50</td>
    <td align="right">16.42</td>
    <td align="right">16.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">12.00</td>
    <td align="right">13.41</td>
    <td align="right">13.41</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">17.52</td>
    <td align="right">23.92</td>
    <td align="right">23.85</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">19.52</td>
    <td align="right">22.11</td>
    <td align="right">22.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">13.73</td>
    <td align="right">16.37</td>
    <td align="right">16.40</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">24.85</td>
    <td align="right">32.73</td>
    <td align="right">32.60</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">27.53</td>
    <td align="right">31.16</td>
    <td align="right">30.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">18.25</td>
    <td align="right">21.01</td>
    <td align="right">21.11</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">28.89</td>
    <td align="right">37.53</td>
    <td align="right">37.56</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">34.45</td>
    <td align="right">37.84</td>
    <td align="right">37.84</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">41.76</td>
    <td align="right">8.60</td>
    <td align="right">6.23</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.03</td>
    <td align="right">54.78</td>
    <td align="right">41.42</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.86</td>
    <td align="right">20.52</td>
    <td align="right">24.88</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.55</td>
    <td align="right">25.91</td>
    <td align="right">29.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">88.98</td>
    <td align="right">85.12</td>
    <td align="right">46.17</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.78</td>
    <td align="right">21.80</td>
    <td align="right">24.32</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">26.79</td>
    <td align="right">28.08</td>
    <td align="right">30.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">109.73</td>
    <td align="right">102.20</td>
    <td align="right">45.49</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.14</td>
    <td align="right">22.72</td>
    <td align="right">24.23</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.42</td>
    <td align="right">30.47</td>
    <td align="right">31.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">138.63</td>
    <td align="right">122.63</td>
    <td align="right">43.75</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.53</td>
    <td align="right">24.28</td>
    <td align="right">25.09</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.13</td>
    <td align="right">33.66</td>
    <td align="right">33.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">89.81</td>
    <td align="right">82.97</td>
    <td align="right">54.42</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">26.81</td>
    <td align="right">25.40</td>
    <td align="right">29.46</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">30.35</td>
    <td align="right">29.81</td>
    <td align="right">32.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">139.53</td>
    <td align="right">121.86</td>
    <td align="right">55.94</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">29.12</td>
    <td align="right">27.15</td>
    <td align="right">29.37</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">31.91</td>
    <td align="right">31.81</td>
    <td align="right">33.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">170.02</td>
    <td align="right">147.64</td>
    <td align="right">54.71</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">30.46</td>
    <td align="right">27.81</td>
    <td align="right">29.21</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">34.67</td>
    <td align="right">35.75</td>
    <td align="right">35.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">218.31</td>
    <td align="right">186.02</td>
    <td align="right">54.89</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">32.39</td>
    <td align="right">29.30</td>
    <td align="right">30.08</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">36.21</td>
    <td align="right">36.05</td>
    <td align="right">36.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.49</td>
    <td align="right">45.84</td>
    <td align="right">45.60</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">26.82</td>
    <td align="right">46.18</td>
    <td align="right">46.39</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.62</td>
    <td align="right">25.35</td>
    <td align="right">25.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">27.99</td>
    <td align="right">61.06</td>
    <td align="right">61.53</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.63</td>
    <td align="right">61.82</td>
    <td align="right">62.09</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.59</td>
    <td align="right">36.26</td>
    <td align="right">25.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.55</td>
    <td align="right">81.21</td>
    <td align="right">83.30</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.96</td>
    <td align="right">83.22</td>
    <td align="right">81.61</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.95</td>
    <td align="right">55.18</td>
    <td align="right">39.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.80</td>
    <td align="right">92.63</td>
    <td align="right">91.89</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">50.86</td>
    <td align="right">97.43</td>
    <td align="right">100.08</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.12</td>
    <td align="right">55.58</td>
    <td align="right">39.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">28.38</td>
    <td align="right">46.51</td>
    <td align="right">47.20</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">32.41</td>
    <td align="right">47.67</td>
    <td align="right">48.28</td>
    <td align="center">5</td>
    <td align="right">2.7313</td>
    <td align="right">22.52</td>
    <td align="right">26.63</td>
    <td align="right">26.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">32.35</td>
    <td align="right">62.64</td>
    <td align="right">63.05</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">39.62</td>
    <td align="right">64.31</td>
    <td align="right">65.42</td>
    <td align="center">8</td>
    <td align="right">0.5366</td>
    <td align="right">22.36</td>
    <td align="right">38.27</td>
    <td align="right">26.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">44.60</td>
    <td align="right">84.77</td>
    <td align="right">85.62</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">50.78</td>
    <td align="right">84.98</td>
    <td align="right">86.39</td>
    <td align="center">11</td>
    <td align="right">0.1134</td>
    <td align="right">31.34</td>
    <td align="right">55.73</td>
    <td align="right">39.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">48.41</td>
    <td align="right">97.47</td>
    <td align="right">96.78</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">56.85</td>
    <td align="right">101.74</td>
    <td align="right">103.05</td>
    <td align="center">13</td>
    <td align="right">0.0253</td>
    <td align="right">31.65</td>
    <td align="right">56.52</td>
    <td align="right">39.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.57</td>
    <td align="right">26.31</td>
    <td align="right">26.06</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.61</td>
    <td align="right">28.97</td>
    <td align="right">28.94</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.78</td>
    <td align="right">31.18</td>
    <td align="right">31.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.87</td>
    <td align="right">46.48</td>
    <td align="right">34.47</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.41</td>
    <td align="right">39.94</td>
    <td align="right">27.52</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">20.60</td>
    <td align="right">51.79</td>
    <td align="right">39.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.87</td>
    <td align="right">54.54</td>
    <td align="right">38.46</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.81</td>
    <td align="right">52.46</td>
    <td align="right">34.69</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.04</td>
    <td align="right">60.96</td>
    <td align="right">43.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.67</td>
    <td align="right">55.01</td>
    <td align="right">39.30</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.45</td>
    <td align="right">65.05</td>
    <td align="right">44.32</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.22</td>
    <td align="right">63.18</td>
    <td align="right">44.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4533</td>
    <td align="right">22.58</td>
    <td align="right">27.39</td>
    <td align="right">27.44</td>
    <td align="center">5</td>
    <td align="right">2.4471</td>
    <td align="right">23.77</td>
    <td align="right">29.16</td>
    <td align="right">29.36</td>
    <td align="center">5</td>
    <td align="right">2.3272</td>
    <td align="right">23.99</td>
    <td align="right">30.34</td>
    <td align="right">30.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4375</td>
    <td align="right">23.24</td>
    <td align="right">47.35</td>
    <td align="right">35.52</td>
    <td align="center">8</td>
    <td align="right">0.4137</td>
    <td align="right">23.16</td>
    <td align="right">39.99</td>
    <td align="right">27.65</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">24.86</td>
    <td align="right">54.10</td>
    <td align="right">39.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0906</td>
    <td align="right">30.90</td>
    <td align="right">55.37</td>
    <td align="right">39.40</td>
    <td align="center">11</td>
    <td align="right">0.0740</td>
    <td align="right">34.55</td>
    <td align="right">62.01</td>
    <td align="right">43.78</td>
    <td align="center">11</td>
    <td align="right">0.0604</td>
    <td align="right">34.24</td>
    <td align="right">61.50</td>
    <td align="right">43.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">31.02</td>
    <td align="right">56.18</td>
    <td align="right">40.07</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">35.07</td>
    <td align="right">65.11</td>
    <td align="right">44.91</td>
    <td align="center">14</td>
    <td align="right">0.0129</td>
    <td align="right">35.00</td>
    <td align="right">65.45</td>
    <td align="right">44.73</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.29</td>
    <td align="right">33.57</td>
    <td align="right">10.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">75.74</td>
    <td align="right">59.47</td>
    <td align="right">46.07</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.78</td>
    <td align="right">21.54</td>
    <td align="right">26.76</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">29.12</td>
    <td align="right">29.05</td>
    <td align="right">32.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">103.48</td>
    <td align="right">102.26</td>
    <td align="right">52.11</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.38</td>
    <td align="right">26.27</td>
    <td align="right">29.26</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">29.88</td>
    <td align="right">30.14</td>
    <td align="right">33.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">164.54</td>
    <td align="right">151.59</td>
    <td align="right">56.09</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">32.35</td>
    <td align="right">28.37</td>
    <td align="right">29.90</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">37.84</td>
    <td align="right">38.89</td>
    <td align="right">39.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">222.22</td>
    <td align="right">196.00</td>
    <td align="right">56.43</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">36.82</td>
    <td align="right">31.73</td>
    <td align="right">32.75</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">41.01</td>
    <td align="right">43.81</td>
    <td align="right">43.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">113.30</td>
    <td align="right">109.04</td>
    <td align="right">64.38</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">30.50</td>
    <td align="right">26.31</td>
    <td align="right">31.46</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">34.74</td>
    <td align="right">37.47</td>
    <td align="right">41.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">188.83</td>
    <td align="right">161.56</td>
    <td align="right">66.35</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">32.36</td>
    <td align="right">27.93</td>
    <td align="right">30.55</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">35.22</td>
    <td align="right">34.38</td>
    <td align="right">36.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">238.78</td>
    <td align="right">205.23</td>
    <td align="right">66.06</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">37.20</td>
    <td align="right">33.02</td>
    <td align="right">34.63</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">43.39</td>
    <td align="right">42.97</td>
    <td align="right">44.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">326.93</td>
    <td align="right">279.39</td>
    <td align="right">69.86</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">42.47</td>
    <td align="right">37.35</td>
    <td align="right">38.10</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">47.15</td>
    <td align="right">47.37</td>
    <td align="right">47.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">26.47</td>
    <td align="right">52.99</td>
    <td align="right">52.94</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.68</td>
    <td align="right">47.37</td>
    <td align="right">47.38</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.09</td>
    <td align="right">30.13</td>
    <td align="right">30.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.45</td>
    <td align="right">65.29</td>
    <td align="right">65.96</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.93</td>
    <td align="right">68.20</td>
    <td align="right">68.48</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">24.76</td>
    <td align="right">46.53</td>
    <td align="right">35.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">48.41</td>
    <td align="right">86.67</td>
    <td align="right">88.83</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">54.89</td>
    <td align="right">90.04</td>
    <td align="right">88.47</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">37.99</td>
    <td align="right">66.57</td>
    <td align="right">50.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">55.14</td>
    <td align="right">100.61</td>
    <td align="right">99.98</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">63.09</td>
    <td align="right">106.92</td>
    <td align="right">109.23</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">40.21</td>
    <td align="right">68.67</td>
    <td align="right">52.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">32.66</td>
    <td align="right">47.37</td>
    <td align="right">48.11</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">37.27</td>
    <td align="right">48.82</td>
    <td align="right">49.34</td>
    <td align="center">5</td>
    <td align="right">2.7250</td>
    <td align="right">25.39</td>
    <td align="right">29.91</td>
    <td align="right">29.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">39.38</td>
    <td align="right">67.24</td>
    <td align="right">67.52</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">42.90</td>
    <td align="right">65.29</td>
    <td align="right">66.24</td>
    <td align="center">8</td>
    <td align="right">0.5385</td>
    <td align="right">28.05</td>
    <td align="right">46.11</td>
    <td align="right">33.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">53.22</td>
    <td align="right">90.62</td>
    <td align="right">91.40</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">60.54</td>
    <td align="right">91.93</td>
    <td align="right">93.11</td>
    <td align="center">11</td>
    <td align="right">0.1183</td>
    <td align="right">40.56</td>
    <td align="right">67.45</td>
    <td align="right">50.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">61.54</td>
    <td align="right">105.87</td>
    <td align="right">104.96</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">69.08</td>
    <td align="right">108.93</td>
    <td align="right">110.24</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">45.06</td>
    <td align="right">70.79</td>
    <td align="right">53.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">19.88</td>
    <td align="right">36.41</td>
    <td align="right">36.43</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">22.37</td>
    <td align="right">33.32</td>
    <td align="right">33.31</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">22.61</td>
    <td align="right">35.73</td>
    <td align="right">35.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">24.39</td>
    <td align="right">55.61</td>
    <td align="right">43.52</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">23.16</td>
    <td align="right">47.34</td>
    <td align="right">34.44</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">27.57</td>
    <td align="right">63.10</td>
    <td align="right">49.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">38.38</td>
    <td align="right">67.21</td>
    <td align="right">51.16</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">41.30</td>
    <td align="right">63.42</td>
    <td align="right">46.03</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">39.89</td>
    <td align="right">71.09</td>
    <td align="right">53.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">39.16</td>
    <td align="right">67.81</td>
    <td align="right">51.77</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">42.50</td>
    <td align="right">77.78</td>
    <td align="right">56.29</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">43.13</td>
    <td align="right">76.80</td>
    <td align="right">57.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4644</td>
    <td align="right">25.41</td>
    <td align="right">31.58</td>
    <td align="right">31.68</td>
    <td align="center">5</td>
    <td align="right">2.4405</td>
    <td align="right">26.63</td>
    <td align="right">32.44</td>
    <td align="right">32.33</td>
    <td align="center">5</td>
    <td align="right">2.3265</td>
    <td align="right">26.76</td>
    <td align="right">34.12</td>
    <td align="right">34.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4413</td>
    <td align="right">25.36</td>
    <td align="right">54.51</td>
    <td align="right">42.59</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">25.11</td>
    <td align="right">42.55</td>
    <td align="right">29.32</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">26.88</td>
    <td align="right">64.11</td>
    <td align="right">49.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0845</td>
    <td align="right">32.39</td>
    <td align="right">58.76</td>
    <td align="right">42.69</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">42.23</td>
    <td align="right">71.93</td>
    <td align="right">53.92</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">41.25</td>
    <td align="right">72.15</td>
    <td align="right">53.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">40.92</td>
    <td align="right">67.32</td>
    <td align="right">51.02</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">43.52</td>
    <td align="right">75.54</td>
    <td align="right">54.98</td>
    <td align="center">14</td>
    <td align="right">0.0116</td>
    <td align="right">43.24</td>
    <td align="right">75.14</td>
    <td align="right">54.96</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
