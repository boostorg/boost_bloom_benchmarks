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
    <td align="right">26.12</td>
    <td align="right">4.47</td>
    <td align="right">3.58</td>
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
    <td align="right">11.05</td>
    <td align="right">10.59</td>
    <td align="right">16.51</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.00</td>
    <td align="right">4.36</td>
    <td align="right">4.36</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.83</td>
    <td align="right">5.05</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.56</td>
    <td align="right">15.63</td>
    <td align="right">17.50</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.79</td>
    <td align="right">4.94</td>
    <td align="right">4.96</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.41</td>
    <td align="right">5.50</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.99</td>
    <td align="right">18.43</td>
    <td align="right">16.41</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.35</td>
    <td align="right">5.28</td>
    <td align="right">5.28</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.22</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.32</td>
    <td align="right">23.43</td>
    <td align="right">16.81</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.36</td>
    <td align="right">6.08</td>
    <td align="right">5.87</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.23</td>
    <td align="right">6.12</td>
    <td align="right">6.11</td>
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
    <td align="right">10.64</td>
    <td align="right">11.02</td>
    <td align="right">16.88</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">3.84</td>
    <td align="right">4.38</td>
    <td align="right">4.38</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.60</td>
    <td align="right">5.21</td>
    <td align="right">5.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.84</td>
    <td align="right">16.15</td>
    <td align="right">17.92</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.40</td>
    <td align="right">5.25</td>
    <td align="right">5.26</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">5.30</td>
    <td align="right">5.78</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.52</td>
    <td align="right">19.36</td>
    <td align="right">17.11</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">4.98</td>
    <td align="right">5.66</td>
    <td align="right">5.60</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.68</td>
    <td align="right">6.43</td>
    <td align="right">6.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">23.39</td>
    <td align="right">24.00</td>
    <td align="right">17.05</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.33</td>
    <td align="right">6.29</td>
    <td align="right">6.29</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">6.19</td>
    <td align="right">6.83</td>
    <td align="right">6.85</td>
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
    <td align="right">5.07</td>
    <td align="right">5.75</td>
    <td align="right">5.74</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.51</td>
    <td align="right">6.69</td>
    <td align="right">6.83</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.94</td>
    <td align="right">3.24</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.00</td>
    <td align="right">8.83</td>
    <td align="right">8.81</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.16</td>
    <td align="right">10.00</td>
    <td align="right">10.05</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.48</td>
    <td align="right">3.11</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.13</td>
    <td align="right">13.71</td>
    <td align="right">13.70</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.62</td>
    <td align="right">14.04</td>
    <td align="right">14.03</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.71</td>
    <td align="right">5.75</td>
    <td align="right">3.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.00</td>
    <td align="right">15.54</td>
    <td align="right">15.49</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.91</td>
    <td align="right">17.51</td>
    <td align="right">17.44</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.76</td>
    <td align="right">5.80</td>
    <td align="right">3.85</td>
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
    <td align="right">4.81</td>
    <td align="right">5.92</td>
    <td align="right">5.92</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">5.69</td>
    <td align="right">6.78</td>
    <td align="right">6.80</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.05</td>
    <td align="right">2.90</td>
    <td align="right">2.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">6.16</td>
    <td align="right">9.06</td>
    <td align="right">9.06</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">7.39</td>
    <td align="right">9.95</td>
    <td align="right">9.97</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.49</td>
    <td align="right">2.71</td>
    <td align="right">2.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">9.09</td>
    <td align="right">13.02</td>
    <td align="right">13.04</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.85</td>
    <td align="right">14.71</td>
    <td align="right">14.69</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.71</td>
    <td align="right">5.98</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">11.19</td>
    <td align="right">15.03</td>
    <td align="right">15.00</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">12.16</td>
    <td align="right">17.52</td>
    <td align="right">17.53</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.78</td>
    <td align="right">6.06</td>
    <td align="right">4.01</td>
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
    <td align="right">2.93</td>
    <td align="right">3.20</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.37</td>
    <td align="right">5.05</td>
    <td align="right">4.99</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.53</td>
    <td align="right">4.95</td>
    <td align="right">5.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.01</td>
    <td align="right">3.28</td>
    <td align="right">3.29</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.19</td>
    <td align="right">4.44</td>
    <td align="right">4.44</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.43</td>
    <td align="right">5.08</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.39</td>
    <td align="right">5.45</td>
    <td align="right">3.76</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.02</td>
    <td align="right">7.61</td>
    <td align="right">5.80</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.81</td>
    <td align="right">7.52</td>
    <td align="right">5.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.44</td>
    <td align="right">5.51</td>
    <td align="right">3.74</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.99</td>
    <td align="right">9.64</td>
    <td align="right">5.95</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.30</td>
    <td align="right">8.97</td>
    <td align="right">5.87</td>
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
    <td align="right">3.06</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.52</td>
    <td align="right">4.73</td>
    <td align="right">4.75</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.55</td>
    <td align="right">4.64</td>
    <td align="right">4.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.21</td>
    <td align="right">2.83</td>
    <td align="right">2.85</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.27</td>
    <td align="right">4.01</td>
    <td align="right">4.00</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.59</td>
    <td align="right">4.77</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.33</td>
    <td align="right">5.65</td>
    <td align="right">3.79</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">7.36</td>
    <td align="right">7.87</td>
    <td align="right">6.00</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">7.84</td>
    <td align="right">7.58</td>
    <td align="right">5.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.41</td>
    <td align="right">5.70</td>
    <td align="right">3.80</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">8.03</td>
    <td align="right">9.20</td>
    <td align="right">6.02</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">8.39</td>
    <td align="right">9.01</td>
    <td align="right">5.94</td>
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
    <td align="right">30.24</td>
    <td align="right">17.51</td>
    <td align="right">6.60</td>
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
    <td align="right">14.06</td>
    <td align="right">13.08</td>
    <td align="right">17.82</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.84</td>
    <td align="right">5.18</td>
    <td align="right">5.46</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.81</td>
    <td align="right">6.01</td>
    <td align="right">6.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.73</td>
    <td align="right">19.07</td>
    <td align="right">18.25</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.65</td>
    <td align="right">5.55</td>
    <td align="right">5.57</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.13</td>
    <td align="right">6.22</td>
    <td align="right">6.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">26.19</td>
    <td align="right">24.36</td>
    <td align="right">17.62</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.57</td>
    <td align="right">6.73</td>
    <td align="right">6.56</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.37</td>
    <td align="right">7.54</td>
    <td align="right">7.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">42.76</td>
    <td align="right">44.23</td>
    <td align="right">20.78</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">14.99</td>
    <td align="right">10.49</td>
    <td align="right">9.11</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.94</td>
    <td align="right">9.82</td>
    <td align="right">9.33</td>
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
    <td align="right">13.35</td>
    <td align="right">13.63</td>
    <td align="right">18.17</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.19</td>
    <td align="right">4.79</td>
    <td align="right">4.82</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">5.58</td>
    <td align="right">6.21</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">18.69</td>
    <td align="right">19.08</td>
    <td align="right">18.59</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">4.61</td>
    <td align="right">5.44</td>
    <td align="right">5.44</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">5.28</td>
    <td align="right">5.79</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">24.62</td>
    <td align="right">24.43</td>
    <td align="right">17.98</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">6.27</td>
    <td align="right">7.18</td>
    <td align="right">7.12</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">7.21</td>
    <td align="right">8.02</td>
    <td align="right">7.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">48.24</td>
    <td align="right">75.87</td>
    <td align="right">22.67</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">10.28</td>
    <td align="right">12.40</td>
    <td align="right">10.21</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">9.35</td>
    <td align="right">10.16</td>
    <td align="right">10.32</td>
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
    <td align="right">6.05</td>
    <td align="right">6.91</td>
    <td align="right">6.90</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.73</td>
    <td align="right">8.12</td>
    <td align="right">8.30</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.58</td>
    <td align="right">4.09</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.04</td>
    <td align="right">9.74</td>
    <td align="right">9.71</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.24</td>
    <td align="right">11.14</td>
    <td align="right">11.01</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.96</td>
    <td align="right">3.80</td>
    <td align="right">4.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.12</td>
    <td align="right">16.00</td>
    <td align="right">15.62</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.00</td>
    <td align="right">16.44</td>
    <td align="right">16.98</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.25</td>
    <td align="right">7.65</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.60</td>
    <td align="right">20.50</td>
    <td align="right">20.12</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.09</td>
    <td align="right">26.11</td>
    <td align="right">22.87</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.47</td>
    <td align="right">10.27</td>
    <td align="right">7.11</td>
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
    <td align="right">5.76</td>
    <td align="right">7.11</td>
    <td align="right">7.11</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">6.87</td>
    <td align="right">8.22</td>
    <td align="right">8.12</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.69</td>
    <td align="right">3.60</td>
    <td align="right">3.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">7.33</td>
    <td align="right">10.93</td>
    <td align="right">10.67</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">8.79</td>
    <td align="right">12.84</td>
    <td align="right">12.44</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.19</td>
    <td align="right">3.52</td>
    <td align="right">3.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">12.49</td>
    <td align="right">15.94</td>
    <td align="right">15.61</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">18.33</td>
    <td align="right">17.71</td>
    <td align="right">17.37</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">8.87</td>
    <td align="right">7.25</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">18.61</td>
    <td align="right">19.59</td>
    <td align="right">19.37</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">16.96</td>
    <td align="right">22.64</td>
    <td align="right">21.89</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">10.58</td>
    <td align="right">11.25</td>
    <td align="right">7.49</td>
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
    <td align="right">3.42</td>
    <td align="right">3.80</td>
    <td align="right">3.80</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.26</td>
    <td align="right">6.17</td>
    <td align="right">6.16</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.36</td>
    <td align="right">6.00</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.51</td>
    <td align="right">3.95</td>
    <td align="right">3.97</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.74</td>
    <td align="right">5.41</td>
    <td align="right">5.18</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.96</td>
    <td align="right">5.85</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.40</td>
    <td align="right">7.27</td>
    <td align="right">4.97</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.38</td>
    <td align="right">9.46</td>
    <td align="right">7.74</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.52</td>
    <td align="right">9.95</td>
    <td align="right">7.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">8.96</td>
    <td align="right">8.87</td>
    <td align="right">8.42</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">12.40</td>
    <td align="right">15.33</td>
    <td align="right">9.10</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.75</td>
    <td align="right">13.97</td>
    <td align="right">9.96</td>
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
    <td align="right">3.78</td>
    <td align="right">3.51</td>
    <td align="right">3.48</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">5.40</td>
    <td align="right">5.67</td>
    <td align="right">5.70</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.49</td>
    <td align="right">5.61</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.63</td>
    <td align="right">3.42</td>
    <td align="right">3.44</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">3.91</td>
    <td align="right">4.61</td>
    <td align="right">4.70</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">4.97</td>
    <td align="right">5.21</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">6.53</td>
    <td align="right">7.21</td>
    <td align="right">4.95</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">9.39</td>
    <td align="right">10.45</td>
    <td align="right">7.92</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">9.57</td>
    <td align="right">9.65</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">8.83</td>
    <td align="right">9.67</td>
    <td align="right">6.85</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">12.13</td>
    <td align="right">15.55</td>
    <td align="right">9.74</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">13.19</td>
    <td align="right">16.51</td>
    <td align="right">10.64</td>
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
    <td align="right">26.46</td>
    <td align="right">4.17</td>
    <td align="right">3.66</td>
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
    <td align="right">9.13</td>
    <td align="right">8.88</td>
    <td align="right">15.29</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.31</td>
    <td align="right">3.94</td>
    <td align="right">3.93</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.85</td>
    <td align="right">4.57</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.97</td>
    <td align="right">14.20</td>
    <td align="right">16.80</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.85</td>
    <td align="right">4.55</td>
    <td align="right">4.54</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.45</td>
    <td align="right">5.25</td>
    <td align="right">5.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.18</td>
    <td align="right">16.55</td>
    <td align="right">15.61</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.32</td>
    <td align="right">5.06</td>
    <td align="right">5.06</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.94</td>
    <td align="right">5.97</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.58</td>
    <td align="right">20.66</td>
    <td align="right">16.14</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.79</td>
    <td align="right">5.84</td>
    <td align="right">5.85</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.87</td>
    <td align="right">3.28</td>
    <td align="right">3.29</td>
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
    <td align="right">10.34</td>
    <td align="right">9.97</td>
    <td align="right">16.40</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">4.20</td>
    <td align="right">4.21</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">3.99</td>
    <td align="right">4.86</td>
    <td align="right">4.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.40</td>
    <td align="right">15.34</td>
    <td align="right">17.05</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.71</td>
    <td align="right">4.73</td>
    <td align="right">4.77</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">4.61</td>
    <td align="right">5.62</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.82</td>
    <td align="right">18.25</td>
    <td align="right">16.47</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">5.13</td>
    <td align="right">5.25</td>
    <td align="right">5.24</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.19</td>
    <td align="right">6.11</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">24.04</td>
    <td align="right">22.89</td>
    <td align="right">16.75</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.61</td>
    <td align="right">6.11</td>
    <td align="right">5.91</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">3.15</td>
    <td align="right">3.48</td>
    <td align="right">3.47</td>
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
    <td align="right">3.04</td>
    <td align="right">3.58</td>
    <td align="right">3.58</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.15</td>
    <td align="right">3.49</td>
    <td align="right">3.47</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.56</td>
    <td align="right">2.46</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.71</td>
    <td align="right">3.36</td>
    <td align="right">3.35</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.72</td>
    <td align="right">3.71</td>
    <td align="right">3.68</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.12</td>
    <td align="right">2.24</td>
    <td align="right">2.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.55</td>
    <td align="right">6.12</td>
    <td align="right">6.13</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.80</td>
    <td align="right">6.07</td>
    <td align="right">6.09</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.13</td>
    <td align="right">4.32</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.01</td>
    <td align="right">6.70</td>
    <td align="right">6.55</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.30</td>
    <td align="right">6.98</td>
    <td align="right">7.18</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.18</td>
    <td align="right">4.35</td>
    <td align="right">3.10</td>
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
    <td align="right">3.18</td>
    <td align="right">3.75</td>
    <td align="right">3.75</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">3.31</td>
    <td align="right">3.66</td>
    <td align="right">3.70</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.88</td>
    <td align="right">2.74</td>
    <td align="right">2.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">3.38</td>
    <td align="right">3.72</td>
    <td align="right">3.67</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.90</td>
    <td align="right">4.01</td>
    <td align="right">3.99</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.78</td>
    <td align="right">2.59</td>
    <td align="right">2.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.81</td>
    <td align="right">6.53</td>
    <td align="right">6.56</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">5.86</td>
    <td align="right">6.67</td>
    <td align="right">6.64</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">4.53</td>
    <td align="right">4.73</td>
    <td align="right">3.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">6.28</td>
    <td align="right">6.79</td>
    <td align="right">6.96</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">6.60</td>
    <td align="right">7.23</td>
    <td align="right">7.14</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">4.51</td>
    <td align="right">4.76</td>
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
    <td align="right">2.60</td>
    <td align="right">2.36</td>
    <td align="right">2.34</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.63</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.68</td>
    <td align="right">3.93</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.71</td>
    <td align="right">2.43</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.95</td>
    <td align="right">3.73</td>
    <td align="right">3.73</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.85</td>
    <td align="right">4.03</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.21</td>
    <td align="right">4.29</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.65</td>
    <td align="right">6.04</td>
    <td align="right">4.62</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.80</td>
    <td align="right">6.01</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.26</td>
    <td align="right">4.31</td>
    <td align="right">2.92</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.64</td>
    <td align="right">7.12</td>
    <td align="right">4.69</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.81</td>
    <td align="right">7.11</td>
    <td align="right">4.63</td>
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
    <td align="right">2.81</td>
    <td align="right">2.68</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">3.81</td>
    <td align="right">4.37</td>
    <td align="right">4.40</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">3.92</td>
    <td align="right">4.34</td>
    <td align="right">4.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">2.96</td>
    <td align="right">2.73</td>
    <td align="right">2.73</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.63</td>
    <td align="right">4.02</td>
    <td align="right">4.03</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.11</td>
    <td align="right">4.32</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.45</td>
    <td align="right">4.59</td>
    <td align="right">3.22</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">5.96</td>
    <td align="right">6.51</td>
    <td align="right">4.99</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">6.01</td>
    <td align="right">6.36</td>
    <td align="right">4.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">4.47</td>
    <td align="right">4.62</td>
    <td align="right">3.20</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.06</td>
    <td align="right">7.51</td>
    <td align="right">5.09</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">7.04</td>
    <td align="right">7.37</td>
    <td align="right">5.08</td>
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
    <td align="right">31.47</td>
    <td align="right">15.55</td>
    <td align="right">6.30</td>
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
    <td align="right">9.98</td>
    <td align="right">9.21</td>
    <td align="right">15.43</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.38</td>
    <td align="right">4.03</td>
    <td align="right">4.05</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.03</td>
    <td align="right">4.61</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">13.58</td>
    <td align="right">13.47</td>
    <td align="right">16.54</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">3.82</td>
    <td align="right">4.57</td>
    <td align="right">4.54</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.48</td>
    <td align="right">5.25</td>
    <td align="right">5.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">18.74</td>
    <td align="right">17.67</td>
    <td align="right">15.41</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">4.94</td>
    <td align="right">5.20</td>
    <td align="right">5.79</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.51</td>
    <td align="right">6.41</td>
    <td align="right">6.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">28.95</td>
    <td align="right">26.54</td>
    <td align="right">18.13</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.49</td>
    <td align="right">8.44</td>
    <td align="right">7.82</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.83</td>
    <td align="right">4.03</td>
    <td align="right">4.24</td>
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
    <td align="right">10.66</td>
    <td align="right">10.04</td>
    <td align="right">16.55</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.32</td>
    <td align="right">4.30</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">4.12</td>
    <td align="right">4.91</td>
    <td align="right">4.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">15.95</td>
    <td align="right">14.77</td>
    <td align="right">17.38</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">5.32</td>
    <td align="right">4.71</td>
    <td align="right">4.76</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">4.72</td>
    <td align="right">5.68</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">20.09</td>
    <td align="right">19.34</td>
    <td align="right">16.58</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">5.42</td>
    <td align="right">6.26</td>
    <td align="right">5.65</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">6.95</td>
    <td align="right">6.76</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">32.28</td>
    <td align="right">30.46</td>
    <td align="right">17.78</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">8.37</td>
    <td align="right">8.82</td>
    <td align="right">8.92</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.18</td>
    <td align="right">4.23</td>
    <td align="right">4.20</td>
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
    <td align="right">3.21</td>
    <td align="right">3.65</td>
    <td align="right">3.65</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.31</td>
    <td align="right">3.57</td>
    <td align="right">3.51</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.72</td>
    <td align="right">2.58</td>
    <td align="right">2.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.73</td>
    <td align="right">3.51</td>
    <td align="right">3.46</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.73</td>
    <td align="right">3.66</td>
    <td align="right">3.72</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.51</td>
    <td align="right">2.27</td>
    <td align="right">2.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">5.58</td>
    <td align="right">6.40</td>
    <td align="right">6.34</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">6.76</td>
    <td align="right">6.83</td>
    <td align="right">7.03</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">4.37</td>
    <td align="right">4.47</td>
    <td align="right">3.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">6.67</td>
    <td align="right">8.06</td>
    <td align="right">7.66</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">7.69</td>
    <td align="right">7.68</td>
    <td align="right">8.29</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">5.59</td>
    <td align="right">6.49</td>
    <td align="right">4.15</td>
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
    <td align="right">3.32</td>
    <td align="right">3.92</td>
    <td align="right">3.88</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">3.47</td>
    <td align="right">3.78</td>
    <td align="right">3.82</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.03</td>
    <td align="right">2.86</td>
    <td align="right">2.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.32</td>
    <td align="right">3.76</td>
    <td align="right">3.63</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">3.91</td>
    <td align="right">4.11</td>
    <td align="right">4.01</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">2.76</td>
    <td align="right">2.61</td>
    <td align="right">2.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">6.11</td>
    <td align="right">6.45</td>
    <td align="right">6.54</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">6.10</td>
    <td align="right">6.67</td>
    <td align="right">6.73</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">4.70</td>
    <td align="right">5.17</td>
    <td align="right">4.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">6.91</td>
    <td align="right">7.55</td>
    <td align="right">7.84</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">7.22</td>
    <td align="right">8.26</td>
    <td align="right">8.26</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">6.42</td>
    <td align="right">7.36</td>
    <td align="right">4.38</td>
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
    <td align="right">2.77</td>
    <td align="right">2.44</td>
    <td align="right">2.43</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">3.85</td>
    <td align="right">4.15</td>
    <td align="right">4.16</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">3.85</td>
    <td align="right">3.99</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.76</td>
    <td align="right">2.49</td>
    <td align="right">2.44</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">2.95</td>
    <td align="right">3.74</td>
    <td align="right">3.68</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">3.89</td>
    <td align="right">4.05</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">4.35</td>
    <td align="right">5.23</td>
    <td align="right">3.05</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.20</td>
    <td align="right">6.81</td>
    <td align="right">6.88</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">6.15</td>
    <td align="right">6.93</td>
    <td align="right">6.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">6.00</td>
    <td align="right">6.71</td>
    <td align="right">3.76</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">9.52</td>
    <td align="right">8.05</td>
    <td align="right">7.14</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">7.94</td>
    <td align="right">8.12</td>
    <td align="right">6.96</td>
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
    <td align="right">2.98</td>
    <td align="right">2.78</td>
    <td align="right">2.79</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.02</td>
    <td align="right">4.42</td>
    <td align="right">4.41</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">4.09</td>
    <td align="right">4.38</td>
    <td align="right">4.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.06</td>
    <td align="right">2.82</td>
    <td align="right">2.82</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">3.60</td>
    <td align="right">4.08</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">4.29</td>
    <td align="right">4.46</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">5.53</td>
    <td align="right">5.84</td>
    <td align="right">6.41</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">6.46</td>
    <td align="right">6.70</td>
    <td align="right">7.12</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">6.57</td>
    <td align="right">6.71</td>
    <td align="right">6.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">6.25</td>
    <td align="right">6.80</td>
    <td align="right">4.29</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.13</td>
    <td align="right">8.74</td>
    <td align="right">7.45</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">8.38</td>
    <td align="right">8.61</td>
    <td align="right">7.39</td>
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
    <td align="right">20.33</td>
    <td align="right">4.26</td>
    <td align="right">3.66</td>
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
    <td align="right">6.76</td>
    <td align="right">4.55</td>
    <td align="right">11.86</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.42</td>
    <td align="right">1.33</td>
    <td align="right">1.29</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.76</td>
    <td align="right">1.39</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.56</td>
    <td align="right">7.69</td>
    <td align="right">12.72</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.46</td>
    <td align="right">1.35</td>
    <td align="right">1.44</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.70</td>
    <td align="right">1.55</td>
    <td align="right">1.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.79</td>
    <td align="right">9.37</td>
    <td align="right">11.91</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.78</td>
    <td align="right">1.75</td>
    <td align="right">1.77</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.91</td>
    <td align="right">1.74</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.68</td>
    <td align="right">11.48</td>
    <td align="right">12.83</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.06</td>
    <td align="right">2.08</td>
    <td align="right">2.04</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.90</td>
    <td align="right">1.75</td>
    <td align="right">1.71</td>
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
    <td align="right">7.44</td>
    <td align="right">4.73</td>
    <td align="right">12.52</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">1.37</td>
    <td align="right">1.25</td>
    <td align="right">1.28</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">1.81</td>
    <td align="right">1.43</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">9.86</td>
    <td align="right">7.81</td>
    <td align="right">13.16</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.59</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">1.81</td>
    <td align="right">1.43</td>
    <td align="right">1.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">14.27</td>
    <td align="right">10.70</td>
    <td align="right">12.21</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">1.77</td>
    <td align="right">1.84</td>
    <td align="right">1.81</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">3.67</td>
    <td align="right">1.81</td>
    <td align="right">1.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">18.57</td>
    <td align="right">10.59</td>
    <td align="right">11.56</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">1.88</td>
    <td align="right">1.97</td>
    <td align="right">1.81</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">2.25</td>
    <td align="right">1.92</td>
    <td align="right">1.75</td>
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
    <td align="right">2.35</td>
    <td align="right">1.75</td>
    <td align="right">1.78</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.38</td>
    <td align="right">3.36</td>
    <td align="right">1.92</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.20</td>
    <td align="right">1.75</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.39</td>
    <td align="right">2.37</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.07</td>
    <td align="right">2.52</td>
    <td align="right">2.49</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.69</td>
    <td align="right">1.50</td>
    <td align="right">1.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.46</td>
    <td align="right">3.22</td>
    <td align="right">3.21</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.31</td>
    <td align="right">3.31</td>
    <td align="right">3.33</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.32</td>
    <td align="right">2.76</td>
    <td align="right">1.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.26</td>
    <td align="right">3.77</td>
    <td align="right">4.20</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.39</td>
    <td align="right">4.24</td>
    <td align="right">4.64</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.36</td>
    <td align="right">3.50</td>
    <td align="right">1.89</td>
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
    <td align="right">2.33</td>
    <td align="right">1.87</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.32</td>
    <td align="right">1.92</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.06</td>
    <td align="right">1.96</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.22</td>
    <td align="right">1.95</td>
    <td align="right">1.94</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">2.80</td>
    <td align="right">2.27</td>
    <td align="right">3.53</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">1.68</td>
    <td align="right">1.52</td>
    <td align="right">1.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">4.47</td>
    <td align="right">3.43</td>
    <td align="right">5.18</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">4.56</td>
    <td align="right">3.20</td>
    <td align="right">3.06</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">3.24</td>
    <td align="right">2.70</td>
    <td align="right">1.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">4.67</td>
    <td align="right">3.64</td>
    <td align="right">3.82</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">5.28</td>
    <td align="right">4.25</td>
    <td align="right">4.26</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">3.28</td>
    <td align="right">3.41</td>
    <td align="right">1.84</td>
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
    <td align="right">2.02</td>
    <td align="right">1.76</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.47</td>
    <td align="right">1.81</td>
    <td align="right">1.83</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.48</td>
    <td align="right">1.88</td>
    <td align="right">1.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.23</td>
    <td align="right">1.88</td>
    <td align="right">1.76</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.27</td>
    <td align="right">2.18</td>
    <td align="right">2.20</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.09</td>
    <td align="right">2.44</td>
    <td align="right">2.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.23</td>
    <td align="right">2.66</td>
    <td align="right">1.88</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.49</td>
    <td align="right">3.10</td>
    <td align="right">3.34</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.41</td>
    <td align="right">3.27</td>
    <td align="right">3.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.22</td>
    <td align="right">3.03</td>
    <td align="right">1.80</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.69</td>
    <td align="right">7.93</td>
    <td align="right">4.33</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.33</td>
    <td align="right">4.06</td>
    <td align="right">3.79</td>
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
    <td align="right">2.02</td>
    <td align="right">1.73</td>
    <td align="right">2.09</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.48</td>
    <td align="right">1.82</td>
    <td align="right">1.77</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.41</td>
    <td align="right">1.85</td>
    <td align="right">1.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">2.24</td>
    <td align="right">1.79</td>
    <td align="right">1.75</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.43</td>
    <td align="right">2.16</td>
    <td align="right">2.17</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.03</td>
    <td align="right">2.36</td>
    <td align="right">2.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.87</td>
    <td align="right">2.67</td>
    <td align="right">1.94</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">4.38</td>
    <td align="right">3.18</td>
    <td align="right">3.32</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">4.68</td>
    <td align="right">3.28</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">3.28</td>
    <td align="right">3.30</td>
    <td align="right">1.95</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">5.22</td>
    <td align="right">4.04</td>
    <td align="right">4.03</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">4.96</td>
    <td align="right">4.09</td>
    <td align="right">4.23</td>
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
    <td align="right">28.84</td>
    <td align="right">13.16</td>
    <td align="right">8.73</td>
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
    <td align="right">9.42</td>
    <td align="right">8.22</td>
    <td align="right">17.01</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.08</td>
    <td align="right">1.90</td>
    <td align="right">2.77</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.54</td>
    <td align="right">2.63</td>
    <td align="right">2.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.06</td>
    <td align="right">22.72</td>
    <td align="right">23.13</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.70</td>
    <td align="right">6.21</td>
    <td align="right">7.05</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.59</td>
    <td align="right">6.15</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">46.59</td>
    <td align="right">40.17</td>
    <td align="right">25.44</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.84</td>
    <td align="right">9.53</td>
    <td align="right">7.94</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.07</td>
    <td align="right">10.02</td>
    <td align="right">9.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">112.80</td>
    <td align="right">82.53</td>
    <td align="right">40.91</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">17.59</td>
    <td align="right">14.17</td>
    <td align="right">17.07</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.95</td>
    <td align="right">13.99</td>
    <td align="right">16.28</td>
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
    <td align="right">17.09</td>
    <td align="right">20.33</td>
    <td align="right">20.09</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">2.59</td>
    <td align="right">3.83</td>
    <td align="right">3.75</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">2.93</td>
    <td align="right">4.03</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">24.98</td>
    <td align="right">22.68</td>
    <td align="right">27.04</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">9.47</td>
    <td align="right">6.80</td>
    <td align="right">5.72</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">6.84</td>
    <td align="right">6.44</td>
    <td align="right">6.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">56.33</td>
    <td align="right">29.55</td>
    <td align="right">19.59</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">6.61</td>
    <td align="right">6.95</td>
    <td align="right">6.99</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">5.81</td>
    <td align="right">5.58</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">50.36</td>
    <td align="right">38.51</td>
    <td align="right">20.34</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">8.32</td>
    <td align="right">7.49</td>
    <td align="right">7.49</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">7.14</td>
    <td align="right">5.99</td>
    <td align="right">6.00</td>
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
    <td align="right">2.77</td>
    <td align="right">2.59</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.75</td>
    <td align="right">2.61</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.44</td>
    <td align="right">2.56</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.75</td>
    <td align="right">4.25</td>
    <td align="right">4.33</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.05</td>
    <td align="right">4.79</td>
    <td align="right">4.49</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.49</td>
    <td align="right">3.39</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">9.73</td>
    <td align="right">8.91</td>
    <td align="right">9.02</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.31</td>
    <td align="right">9.03</td>
    <td align="right">9.08</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.27</td>
    <td align="right">7.29</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.59</td>
    <td align="right">13.38</td>
    <td align="right">13.36</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.78</td>
    <td align="right">13.66</td>
    <td align="right">13.63</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.47</td>
    <td align="right">11.05</td>
    <td align="right">7.02</td>
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
    <td align="right">2.74</td>
    <td align="right">2.61</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.77</td>
    <td align="right">2.61</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">2.41</td>
    <td align="right">2.53</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.77</td>
    <td align="right">4.43</td>
    <td align="right">4.14</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.04</td>
    <td align="right">4.80</td>
    <td align="right">4.52</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">2.56</td>
    <td align="right">3.20</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">9.64</td>
    <td align="right">11.17</td>
    <td align="right">8.87</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">9.63</td>
    <td align="right">8.61</td>
    <td align="right">9.40</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">7.84</td>
    <td align="right">8.14</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">14.47</td>
    <td align="right">13.26</td>
    <td align="right">13.21</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">14.66</td>
    <td align="right">13.39</td>
    <td align="right">14.39</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">9.48</td>
    <td align="right">10.25</td>
    <td align="right">6.30</td>
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
    <td align="right">2.41</td>
    <td align="right">2.52</td>
    <td align="right">2.51</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.74</td>
    <td align="right">2.57</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.75</td>
    <td align="right">2.64</td>
    <td align="right">2.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.82</td>
    <td align="right">3.00</td>
    <td align="right">2.89</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.76</td>
    <td align="right">4.60</td>
    <td align="right">3.97</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.07</td>
    <td align="right">4.79</td>
    <td align="right">4.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.48</td>
    <td align="right">8.01</td>
    <td align="right">5.11</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">9.66</td>
    <td align="right">8.83</td>
    <td align="right">8.85</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.22</td>
    <td align="right">8.55</td>
    <td align="right">8.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.49</td>
    <td align="right">10.28</td>
    <td align="right">6.03</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.22</td>
    <td align="right">13.31</td>
    <td align="right">13.26</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.70</td>
    <td align="right">13.58</td>
    <td align="right">13.58</td>
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
    <td align="right">2.39</td>
    <td align="right">2.83</td>
    <td align="right">2.71</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">2.75</td>
    <td align="right">2.57</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.75</td>
    <td align="right">2.62</td>
    <td align="right">2.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">2.80</td>
    <td align="right">3.01</td>
    <td align="right">2.93</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.72</td>
    <td align="right">4.13</td>
    <td align="right">4.10</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.05</td>
    <td align="right">4.53</td>
    <td align="right">4.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">7.32</td>
    <td align="right">7.37</td>
    <td align="right">5.08</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">9.61</td>
    <td align="right">8.83</td>
    <td align="right">8.86</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">16.13</td>
    <td align="right">15.70</td>
    <td align="right">11.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">9.40</td>
    <td align="right">10.32</td>
    <td align="right">6.04</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">14.34</td>
    <td align="right">13.22</td>
    <td align="right">13.26</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">14.75</td>
    <td align="right">13.49</td>
    <td align="right">13.58</td>
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
    <td align="right">34.67</td>
    <td align="right">5.55</td>
    <td align="right">3.50</td>
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
    <td align="right">12.14</td>
    <td align="right">12.40</td>
    <td align="right">16.95</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.82</td>
    <td align="right">4.22</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.95</td>
    <td align="right">5.51</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.45</td>
    <td align="right">17.87</td>
    <td align="right">17.57</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.94</td>
    <td align="right">4.90</td>
    <td align="right">4.76</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.05</td>
    <td align="right">5.94</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.63</td>
    <td align="right">21.24</td>
    <td align="right">16.61</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.64</td>
    <td align="right">5.55</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.30</td>
    <td align="right">6.68</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.05</td>
    <td align="right">27.43</td>
    <td align="right">17.23</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.89</td>
    <td align="right">6.15</td>
    <td align="right">5.88</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.35</td>
    <td align="right">7.39</td>
    <td align="right">7.38</td>
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
    <td align="right">13.56</td>
    <td align="right">13.87</td>
    <td align="right">18.59</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">5.97</td>
    <td align="right">4.49</td>
    <td align="right">4.47</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">7.12</td>
    <td align="right">5.58</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">20.90</td>
    <td align="right">19.50</td>
    <td align="right">18.69</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">7.22</td>
    <td align="right">4.91</td>
    <td align="right">4.89</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">8.40</td>
    <td align="right">6.12</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">26.34</td>
    <td align="right">23.90</td>
    <td align="right">17.75</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">8.95</td>
    <td align="right">5.49</td>
    <td align="right">5.68</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">9.71</td>
    <td align="right">6.94</td>
    <td align="right">6.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">34.56</td>
    <td align="right">30.57</td>
    <td align="right">18.16</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">10.08</td>
    <td align="right">6.08</td>
    <td align="right">6.09</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">10.87</td>
    <td align="right">7.57</td>
    <td align="right">7.67</td>
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
    <td align="right">5.61</td>
    <td align="right">5.69</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.15</td>
    <td align="right">5.55</td>
    <td align="right">5.66</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.38</td>
    <td align="right">3.93</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.75</td>
    <td align="right">8.45</td>
    <td align="right">8.54</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.43</td>
    <td align="right">8.68</td>
    <td align="right">8.70</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.92</td>
    <td align="right">4.85</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.69</td>
    <td align="right">11.00</td>
    <td align="right">10.79</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.90</td>
    <td align="right">10.46</td>
    <td align="right">11.20</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.99</td>
    <td align="right">7.03</td>
    <td align="right">5.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.50</td>
    <td align="right">13.89</td>
    <td align="right">13.91</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.34</td>
    <td align="right">13.64</td>
    <td align="right">12.69</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.09</td>
    <td align="right">7.07</td>
    <td align="right">5.32</td>
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
    <td align="right">7.98</td>
    <td align="right">5.72</td>
    <td align="right">5.72</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">9.19</td>
    <td align="right">5.44</td>
    <td align="right">5.41</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.45</td>
    <td align="right">4.02</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">11.21</td>
    <td align="right">8.65</td>
    <td align="right">8.66</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">19.33</td>
    <td align="right">8.80</td>
    <td align="right">7.92</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.98</td>
    <td align="right">4.93</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">15.65</td>
    <td align="right">11.01</td>
    <td align="right">11.31</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.05</td>
    <td align="right">10.69</td>
    <td align="right">10.74</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.17</td>
    <td align="right">7.13</td>
    <td align="right">5.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">17.32</td>
    <td align="right">14.40</td>
    <td align="right">14.41</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">19.24</td>
    <td align="right">13.93</td>
    <td align="right">13.97</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.28</td>
    <td align="right">7.12</td>
    <td align="right">5.38</td>
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
    <td align="right">3.32</td>
    <td align="right">3.83</td>
    <td align="right">3.84</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.44</td>
    <td align="right">5.46</td>
    <td align="right">5.48</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.62</td>
    <td align="right">5.46</td>
    <td align="right">5.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.29</td>
    <td align="right">5.59</td>
    <td align="right">4.74</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.75</td>
    <td align="right">5.85</td>
    <td align="right">5.12</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.97</td>
    <td align="right">6.99</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.01</td>
    <td align="right">6.87</td>
    <td align="right">5.18</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.85</td>
    <td align="right">9.39</td>
    <td align="right">7.63</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.88</td>
    <td align="right">9.23</td>
    <td align="right">7.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.09</td>
    <td align="right">6.89</td>
    <td align="right">5.08</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.11</td>
    <td align="right">10.45</td>
    <td align="right">7.55</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.05</td>
    <td align="right">10.18</td>
    <td align="right">7.38</td>
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
    <td align="right">3.89</td>
    <td align="right">3.88</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.51</td>
    <td align="right">5.54</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.63</td>
    <td align="right">5.35</td>
    <td align="right">5.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.34</td>
    <td align="right">5.50</td>
    <td align="right">4.63</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">4.79</td>
    <td align="right">5.98</td>
    <td align="right">5.06</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">6.96</td>
    <td align="right">7.09</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.10</td>
    <td align="right">6.92</td>
    <td align="right">5.16</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">9.69</td>
    <td align="right">9.53</td>
    <td align="right">7.71</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">9.82</td>
    <td align="right">9.14</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.16</td>
    <td align="right">6.90</td>
    <td align="right">5.12</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">10.22</td>
    <td align="right">10.60</td>
    <td align="right">7.76</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">10.20</td>
    <td align="right">10.47</td>
    <td align="right">7.57</td>
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
    <td align="right">43.52</td>
    <td align="right">20.64</td>
    <td align="right">9.19</td>
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
    <td align="right">14.57</td>
    <td align="right">13.01</td>
    <td align="right">17.75</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.02</td>
    <td align="right">4.47</td>
    <td align="right">4.58</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.02</td>
    <td align="right">5.64</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">24.12</td>
    <td align="right">20.26</td>
    <td align="right">18.84</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.63</td>
    <td align="right">5.40</td>
    <td align="right">5.46</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.21</td>
    <td align="right">7.00</td>
    <td align="right">6.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">42.74</td>
    <td align="right">39.62</td>
    <td align="right">19.63</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">14.17</td>
    <td align="right">9.66</td>
    <td align="right">9.48</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">15.11</td>
    <td align="right">12.59</td>
    <td align="right">12.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">72.46</td>
    <td align="right">94.46</td>
    <td align="right">26.57</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">22.55</td>
    <td align="right">21.63</td>
    <td align="right">20.46</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">25.93</td>
    <td align="right">22.90</td>
    <td align="right">23.02</td>
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
    <td align="right">15.79</td>
    <td align="right">14.41</td>
    <td align="right">19.03</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">7.34</td>
    <td align="right">4.65</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">8.62</td>
    <td align="right">5.97</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">25.33</td>
    <td align="right">22.46</td>
    <td align="right">20.55</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">9.84</td>
    <td align="right">6.23</td>
    <td align="right">5.89</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">11.98</td>
    <td align="right">7.16</td>
    <td align="right">7.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">47.51</td>
    <td align="right">44.41</td>
    <td align="right">22.69</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">16.20</td>
    <td align="right">12.08</td>
    <td align="right">11.90</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">20.62</td>
    <td align="right">15.74</td>
    <td align="right">10.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">96.61</td>
    <td align="right">95.80</td>
    <td align="right">26.23</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">22.25</td>
    <td align="right">16.14</td>
    <td align="right">17.04</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">23.44</td>
    <td align="right">11.73</td>
    <td align="right">13.57</td>
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
    <td align="right">9.24</td>
    <td align="right">6.28</td>
    <td align="right">6.27</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">10.64</td>
    <td align="right">6.32</td>
    <td align="right">6.24</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.84</td>
    <td align="right">4.23</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.80</td>
    <td align="right">9.85</td>
    <td align="right">10.13</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.50</td>
    <td align="right">9.25</td>
    <td align="right">9.26</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.30</td>
    <td align="right">5.23</td>
    <td align="right">4.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.63</td>
    <td align="right">13.64</td>
    <td align="right">12.96</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.17</td>
    <td align="right">11.41</td>
    <td align="right">11.73</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.62</td>
    <td align="right">9.08</td>
    <td align="right">6.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">26.04</td>
    <td align="right">19.76</td>
    <td align="right">28.73</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.93</td>
    <td align="right">20.00</td>
    <td align="right">19.10</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">8.98</td>
    <td align="right">11.27</td>
    <td align="right">9.09</td>
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
    <td align="right">9.33</td>
    <td align="right">6.32</td>
    <td align="right">6.32</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">14.11</td>
    <td align="right">5.92</td>
    <td align="right">5.67</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.77</td>
    <td align="right">4.25</td>
    <td align="right">4.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">13.52</td>
    <td align="right">10.41</td>
    <td align="right">10.07</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">15.42</td>
    <td align="right">9.21</td>
    <td align="right">8.49</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.27</td>
    <td align="right">5.25</td>
    <td align="right">4.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">17.80</td>
    <td align="right">12.87</td>
    <td align="right">13.50</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">17.65</td>
    <td align="right">12.03</td>
    <td align="right">12.02</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">5.91</td>
    <td align="right">7.63</td>
    <td align="right">5.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">20.89</td>
    <td align="right">17.19</td>
    <td align="right">17.21</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">23.94</td>
    <td align="right">18.27</td>
    <td align="right">18.03</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">7.86</td>
    <td align="right">10.31</td>
    <td align="right">8.14</td>
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
    <td align="right">3.68</td>
    <td align="right">4.09</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.86</td>
    <td align="right">5.86</td>
    <td align="right">5.88</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.17</td>
    <td align="right">5.79</td>
    <td align="right">5.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.55</td>
    <td align="right">5.92</td>
    <td align="right">4.97</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.34</td>
    <td align="right">6.26</td>
    <td align="right">5.48</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.54</td>
    <td align="right">7.44</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.86</td>
    <td align="right">7.63</td>
    <td align="right">5.66</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.70</td>
    <td align="right">10.09</td>
    <td align="right">8.16</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.97</td>
    <td align="right">10.52</td>
    <td align="right">8.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.57</td>
    <td align="right">9.20</td>
    <td align="right">6.64</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">13.64</td>
    <td align="right">14.56</td>
    <td align="right">10.61</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.75</td>
    <td align="right">12.98</td>
    <td align="right">9.79</td>
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
    <td align="right">3.64</td>
    <td align="right">4.10</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.96</td>
    <td align="right">5.88</td>
    <td align="right">5.87</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.03</td>
    <td align="right">5.71</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.74</td>
    <td align="right">5.91</td>
    <td align="right">4.95</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">5.42</td>
    <td align="right">6.56</td>
    <td align="right">5.63</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">7.83</td>
    <td align="right">8.30</td>
    <td align="right">6.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">6.60</td>
    <td align="right">12.57</td>
    <td align="right">7.68</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">11.66</td>
    <td align="right">11.42</td>
    <td align="right">8.65</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">11.44</td>
    <td align="right">10.92</td>
    <td align="right">9.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">13.44</td>
    <td align="right">18.37</td>
    <td align="right">13.79</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">17.89</td>
    <td align="right">25.64</td>
    <td align="right">12.15</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">17.60</td>
    <td align="right">19.64</td>
    <td align="right">14.82</td>
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
    <td align="right">62.51</td>
    <td align="right">29.90</td>
    <td align="right">14.44</td>
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
    <td align="right">27.16</td>
    <td align="right">41.63</td>
    <td align="right">36.37</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.45</td>
    <td align="right">15.92</td>
    <td align="right">15.93</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.08</td>
    <td align="right">19.69</td>
    <td align="right">19.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.95</td>
    <td align="right">63.41</td>
    <td align="right">39.30</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.26</td>
    <td align="right">19.37</td>
    <td align="right">19.31</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.08</td>
    <td align="right">18.66</td>
    <td align="right">18.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.58</td>
    <td align="right">77.36</td>
    <td align="right">38.19</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.19</td>
    <td align="right">18.45</td>
    <td align="right">18.44</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.05</td>
    <td align="right">18.22</td>
    <td align="right">18.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">55.84</td>
    <td align="right">96.08</td>
    <td align="right">37.38</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.18</td>
    <td align="right">18.76</td>
    <td align="right">18.81</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.98</td>
    <td align="right">19.99</td>
    <td align="right">20.00</td>
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
    <td align="right">27.85</td>
    <td align="right">40.18</td>
    <td align="right">37.09</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">12.25</td>
    <td align="right">15.45</td>
    <td align="right">15.44</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">13.73</td>
    <td align="right">16.20</td>
    <td align="right">16.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">42.13</td>
    <td align="right">58.63</td>
    <td align="right">39.48</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">14.50</td>
    <td align="right">17.10</td>
    <td align="right">17.18</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">15.08</td>
    <td align="right">17.23</td>
    <td align="right">17.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">51.65</td>
    <td align="right">73.39</td>
    <td align="right">38.68</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.70</td>
    <td align="right">17.62</td>
    <td align="right">17.63</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">16.56</td>
    <td align="right">17.54</td>
    <td align="right">17.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">64.66</td>
    <td align="right">98.12</td>
    <td align="right">41.22</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">16.48</td>
    <td align="right">17.74</td>
    <td align="right">18.36</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">16.08</td>
    <td align="right">19.12</td>
    <td align="right">19.16</td>
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
    <td align="right">16.09</td>
    <td align="right">20.50</td>
    <td align="right">20.48</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.54</td>
    <td align="right">22.13</td>
    <td align="right">22.16</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.53</td>
    <td align="right">13.55</td>
    <td align="right">13.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.14</td>
    <td align="right">26.72</td>
    <td align="right">26.70</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.44</td>
    <td align="right">28.87</td>
    <td align="right">28.97</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.80</td>
    <td align="right">16.46</td>
    <td align="right">15.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.83</td>
    <td align="right">32.94</td>
    <td align="right">32.93</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.95</td>
    <td align="right">45.65</td>
    <td align="right">45.69</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.50</td>
    <td align="right">19.46</td>
    <td align="right">19.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.40</td>
    <td align="right">35.96</td>
    <td align="right">35.92</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.19</td>
    <td align="right">55.44</td>
    <td align="right">55.42</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.78</td>
    <td align="right">24.56</td>
    <td align="right">24.56</td>
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
    <td align="right">17.23</td>
    <td align="right">20.52</td>
    <td align="right">20.55</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.42</td>
    <td align="right">20.69</td>
    <td align="right">20.78</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">11.37</td>
    <td align="right">14.23</td>
    <td align="right">14.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.46</td>
    <td align="right">26.61</td>
    <td align="right">26.60</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">39.96</td>
    <td align="right">27.75</td>
    <td align="right">27.77</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">13.70</td>
    <td align="right">18.12</td>
    <td align="right">18.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.38</td>
    <td align="right">34.67</td>
    <td align="right">34.21</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">67.48</td>
    <td align="right">46.02</td>
    <td align="right">45.91</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">16.21</td>
    <td align="right">20.23</td>
    <td align="right">19.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">34.63</td>
    <td align="right">36.64</td>
    <td align="right">36.73</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.30</td>
    <td align="right">55.11</td>
    <td align="right">55.06</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">25.16</td>
    <td align="right">25.26</td>
    <td align="right">25.25</td>
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
    <td align="right">14.45</td>
    <td align="right">16.00</td>
    <td align="right">15.64</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.11</td>
    <td align="right">20.51</td>
    <td align="right">20.52</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.49</td>
    <td align="right">22.12</td>
    <td align="right">22.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.03</td>
    <td align="right">20.15</td>
    <td align="right">20.16</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.09</td>
    <td align="right">26.76</td>
    <td align="right">26.74</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.37</td>
    <td align="right">29.02</td>
    <td align="right">29.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.55</td>
    <td align="right">25.03</td>
    <td align="right">25.04</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.77</td>
    <td align="right">33.18</td>
    <td align="right">33.17</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.94</td>
    <td align="right">45.73</td>
    <td align="right">45.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">33.92</td>
    <td align="right">34.86</td>
    <td align="right">34.84</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.38</td>
    <td align="right">36.00</td>
    <td align="right">36.21</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.00</td>
    <td align="right">55.36</td>
    <td align="right">55.36</td>
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
    <td align="right">14.90</td>
    <td align="right">16.02</td>
    <td align="right">16.00</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">17.32</td>
    <td align="right">20.59</td>
    <td align="right">20.54</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.44</td>
    <td align="right">20.76</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">20.14</td>
    <td align="right">20.14</td>
    <td align="right">20.19</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.30</td>
    <td align="right">26.58</td>
    <td align="right">26.60</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">39.92</td>
    <td align="right">27.77</td>
    <td align="right">27.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">28.39</td>
    <td align="right">23.21</td>
    <td align="right">23.21</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.43</td>
    <td align="right">34.64</td>
    <td align="right">34.11</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">67.43</td>
    <td align="right">45.94</td>
    <td align="right">46.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">34.36</td>
    <td align="right">34.79</td>
    <td align="right">34.77</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">34.61</td>
    <td align="right">36.74</td>
    <td align="right">37.37</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.50</td>
    <td align="right">55.06</td>
    <td align="right">55.04</td>
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
    <td align="right">73.67</td>
    <td align="right">102.84</td>
    <td align="right">18.33</td>
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
    <td align="right">28.16</td>
    <td align="right">43.57</td>
    <td align="right">39.76</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.94</td>
    <td align="right">16.34</td>
    <td align="right">16.30</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.48</td>
    <td align="right">19.84</td>
    <td align="right">19.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">38.17</td>
    <td align="right">64.66</td>
    <td align="right">41.33</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.74</td>
    <td align="right">20.76</td>
    <td align="right">20.65</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">17.45</td>
    <td align="right">19.44</td>
    <td align="right">19.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">50.79</td>
    <td align="right">95.27</td>
    <td align="right">42.82</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">19.77</td>
    <td align="right">22.09</td>
    <td align="right">21.77</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">22.29</td>
    <td align="right">23.51</td>
    <td align="right">25.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">82.85</td>
    <td align="right">163.67</td>
    <td align="right">62.66</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">25.26</td>
    <td align="right">27.67</td>
    <td align="right">28.22</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">27.29</td>
    <td align="right">27.29</td>
    <td align="right">28.32</td>
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
    <td align="right">28.36</td>
    <td align="right">41.77</td>
    <td align="right">40.56</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">12.42</td>
    <td align="right">15.76</td>
    <td align="right">15.74</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.00</td>
    <td align="right">16.71</td>
    <td align="right">16.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">42.80</td>
    <td align="right">60.90</td>
    <td align="right">44.51</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">16.66</td>
    <td align="right">18.69</td>
    <td align="right">19.97</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">15.46</td>
    <td align="right">17.62</td>
    <td align="right">17.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">56.84</td>
    <td align="right">76.25</td>
    <td align="right">41.01</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">17.69</td>
    <td align="right">19.25</td>
    <td align="right">19.08</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">18.41</td>
    <td align="right">19.63</td>
    <td align="right">20.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">121.87</td>
    <td align="right">197.34</td>
    <td align="right">56.12</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">28.98</td>
    <td align="right">29.35</td>
    <td align="right">28.89</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">28.89</td>
    <td align="right">29.35</td>
    <td align="right">30.89</td>
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
    <td align="right">17.09</td>
    <td align="right">21.57</td>
    <td align="right">21.23</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.57</td>
    <td align="right">23.11</td>
    <td align="right">23.23</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.92</td>
    <td align="right">14.14</td>
    <td align="right">13.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.05</td>
    <td align="right">26.16</td>
    <td align="right">26.47</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.95</td>
    <td align="right">30.04</td>
    <td align="right">30.51</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.86</td>
    <td align="right">16.71</td>
    <td align="right">16.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">37.53</td>
    <td align="right">59.46</td>
    <td align="right">49.68</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">78.10</td>
    <td align="right">81.70</td>
    <td align="right">70.16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">37.27</td>
    <td align="right">54.89</td>
    <td align="right">50.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">72.85</td>
    <td align="right">89.14</td>
    <td align="right">98.51</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">127.18</td>
    <td align="right">103.16</td>
    <td align="right">107.38</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.95</td>
    <td align="right">60.12</td>
    <td align="right">48.61</td>
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
    <td align="right">18.15</td>
    <td align="right">23.61</td>
    <td align="right">22.14</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">32.95</td>
    <td align="right">23.66</td>
    <td align="right">23.43</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">11.81</td>
    <td align="right">15.31</td>
    <td align="right">15.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">26.15</td>
    <td align="right">27.75</td>
    <td align="right">27.66</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">47.28</td>
    <td align="right">32.84</td>
    <td align="right">35.67</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">14.11</td>
    <td align="right">18.96</td>
    <td align="right">19.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">41.30</td>
    <td align="right">49.34</td>
    <td align="right">49.26</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">73.97</td>
    <td align="right">53.66</td>
    <td align="right">52.86</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">19.83</td>
    <td align="right">27.78</td>
    <td align="right">26.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">53.05</td>
    <td align="right">67.73</td>
    <td align="right">66.59</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">98.36</td>
    <td align="right">73.28</td>
    <td align="right">70.86</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">48.54</td>
    <td align="right">56.03</td>
    <td align="right">56.83</td>
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
    <td align="right">15.82</td>
    <td align="right">16.87</td>
    <td align="right">16.44</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.12</td>
    <td align="right">21.28</td>
    <td align="right">21.68</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">37.01</td>
    <td align="right">24.36</td>
    <td align="right">23.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">20.84</td>
    <td align="right">23.67</td>
    <td align="right">22.51</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.95</td>
    <td align="right">29.72</td>
    <td align="right">28.53</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">54.31</td>
    <td align="right">32.11</td>
    <td align="right">37.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">37.93</td>
    <td align="right">32.42</td>
    <td align="right">35.67</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.02</td>
    <td align="right">41.31</td>
    <td align="right">41.24</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">75.92</td>
    <td align="right">74.77</td>
    <td align="right">71.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">87.77</td>
    <td align="right">96.96</td>
    <td align="right">86.50</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">54.42</td>
    <td align="right">58.67</td>
    <td align="right">71.28</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">109.30</td>
    <td align="right">79.02</td>
    <td align="right">80.21</td>
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
    <td align="right">16.18</td>
    <td align="right">16.61</td>
    <td align="right">16.67</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">17.87</td>
    <td align="right">21.87</td>
    <td align="right">21.91</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">32.15</td>
    <td align="right">22.28</td>
    <td align="right">22.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">21.29</td>
    <td align="right">21.87</td>
    <td align="right">21.38</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">22.10</td>
    <td align="right">26.83</td>
    <td align="right">29.54</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">49.90</td>
    <td align="right">31.95</td>
    <td align="right">30.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">37.54</td>
    <td align="right">30.12</td>
    <td align="right">28.74</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">35.90</td>
    <td align="right">46.76</td>
    <td align="right">41.69</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">71.14</td>
    <td align="right">51.03</td>
    <td align="right">49.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">70.31</td>
    <td align="right">93.17</td>
    <td align="right">92.21</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">53.22</td>
    <td align="right">85.87</td>
    <td align="right">88.00</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">111.89</td>
    <td align="right">86.49</td>
    <td align="right">83.91</td>
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
    <td align="right">61.48</td>
    <td align="right">10.33</td>
    <td align="right">7.25</td>
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
    <td align="right">13.80</td>
    <td align="right">22.80</td>
    <td align="right">26.58</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.61</td>
    <td align="right">12.34</td>
    <td align="right">12.36</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.68</td>
    <td align="right">13.84</td>
    <td align="right">13.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.56</td>
    <td align="right">35.23</td>
    <td align="right">28.87</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.11</td>
    <td align="right">14.10</td>
    <td align="right">14.12</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.49</td>
    <td align="right">15.32</td>
    <td align="right">15.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.23</td>
    <td align="right">47.52</td>
    <td align="right">29.96</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.73</td>
    <td align="right">15.37</td>
    <td align="right">15.33</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.65</td>
    <td align="right">16.82</td>
    <td align="right">16.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.17</td>
    <td align="right">60.39</td>
    <td align="right">30.90</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.63</td>
    <td align="right">16.32</td>
    <td align="right">16.31</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.85</td>
    <td align="right">17.86</td>
    <td align="right">17.77</td>
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
    <td align="right">19.12</td>
    <td align="right">27.69</td>
    <td align="right">28.41</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">9.60</td>
    <td align="right">12.42</td>
    <td align="right">12.39</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">12.62</td>
    <td align="right">14.68</td>
    <td align="right">14.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">28.13</td>
    <td align="right">41.77</td>
    <td align="right">30.82</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">12.78</td>
    <td align="right">15.00</td>
    <td align="right">14.95</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">14.40</td>
    <td align="right">15.89</td>
    <td align="right">15.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">34.43</td>
    <td align="right">53.38</td>
    <td align="right">30.14</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.58</td>
    <td align="right">16.27</td>
    <td align="right">16.25</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">15.33</td>
    <td align="right">17.25</td>
    <td align="right">17.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">48.08</td>
    <td align="right">67.83</td>
    <td align="right">31.79</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">15.48</td>
    <td align="right">17.26</td>
    <td align="right">17.29</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">17.29</td>
    <td align="right">19.03</td>
    <td align="right">19.02</td>
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
    <td align="right">12.72</td>
    <td align="right">16.09</td>
    <td align="right">16.10</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.22</td>
    <td align="right">16.68</td>
    <td align="right">16.71</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.09</td>
    <td align="right">9.35</td>
    <td align="right">9.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.37</td>
    <td align="right">22.56</td>
    <td align="right">22.57</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.31</td>
    <td align="right">22.32</td>
    <td align="right">22.32</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.17</td>
    <td align="right">13.96</td>
    <td align="right">13.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.97</td>
    <td align="right">32.15</td>
    <td align="right">32.13</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.62</td>
    <td align="right">30.65</td>
    <td align="right">30.60</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.47</td>
    <td align="right">17.60</td>
    <td align="right">17.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.85</td>
    <td align="right">35.77</td>
    <td align="right">35.72</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.05</td>
    <td align="right">35.90</td>
    <td align="right">35.77</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.26</td>
    <td align="right">20.51</td>
    <td align="right">20.45</td>
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
    <td align="right">13.17</td>
    <td align="right">16.90</td>
    <td align="right">16.92</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.20</td>
    <td align="right">16.29</td>
    <td align="right">16.33</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">7.09</td>
    <td align="right">9.35</td>
    <td align="right">9.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">17.92</td>
    <td align="right">25.48</td>
    <td align="right">25.50</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">19.49</td>
    <td align="right">23.68</td>
    <td align="right">23.68</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">10.91</td>
    <td align="right">13.47</td>
    <td align="right">13.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">24.94</td>
    <td align="right">32.72</td>
    <td align="right">32.55</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.71</td>
    <td align="right">31.25</td>
    <td align="right">30.92</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">13.17</td>
    <td align="right">17.98</td>
    <td align="right">17.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.38</td>
    <td align="right">36.15</td>
    <td align="right">36.10</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">34.13</td>
    <td align="right">38.30</td>
    <td align="right">38.24</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">17.41</td>
    <td align="right">20.80</td>
    <td align="right">20.75</td>
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
    <td align="right">6.54</td>
    <td align="right">9.34</td>
    <td align="right">9.36</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.86</td>
    <td align="right">16.15</td>
    <td align="right">16.12</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.22</td>
    <td align="right">16.70</td>
    <td align="right">16.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.93</td>
    <td align="right">13.67</td>
    <td align="right">13.73</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.42</td>
    <td align="right">22.55</td>
    <td align="right">22.57</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.29</td>
    <td align="right">22.36</td>
    <td align="right">22.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.71</td>
    <td align="right">17.60</td>
    <td align="right">17.64</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.91</td>
    <td align="right">32.11</td>
    <td align="right">32.11</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.55</td>
    <td align="right">30.60</td>
    <td align="right">30.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.09</td>
    <td align="right">21.13</td>
    <td align="right">21.03</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.22</td>
    <td align="right">35.73</td>
    <td align="right">35.84</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.07</td>
    <td align="right">35.82</td>
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
    <td align="right">6.72</td>
    <td align="right">9.49</td>
    <td align="right">9.47</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">13.58</td>
    <td align="right">16.91</td>
    <td align="right">16.92</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.20</td>
    <td align="right">16.28</td>
    <td align="right">16.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">10.01</td>
    <td align="right">13.82</td>
    <td align="right">13.88</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">17.96</td>
    <td align="right">25.53</td>
    <td align="right">25.55</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">19.50</td>
    <td align="right">23.77</td>
    <td align="right">23.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">14.19</td>
    <td align="right">17.54</td>
    <td align="right">17.53</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">24.98</td>
    <td align="right">32.74</td>
    <td align="right">32.51</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.69</td>
    <td align="right">31.24</td>
    <td align="right">30.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">17.66</td>
    <td align="right">20.63</td>
    <td align="right">20.68</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.47</td>
    <td align="right">36.09</td>
    <td align="right">36.30</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">34.10</td>
    <td align="right">38.30</td>
    <td align="right">38.30</td>
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
    <td align="right">78.62</td>
    <td align="right">46.45</td>
    <td align="right">10.77</td>
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
    <td align="right">14.13</td>
    <td align="right">22.85</td>
    <td align="right">28.22</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.69</td>
    <td align="right">12.57</td>
    <td align="right">12.53</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.78</td>
    <td align="right">14.03</td>
    <td align="right">14.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.58</td>
    <td align="right">35.15</td>
    <td align="right">29.59</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.08</td>
    <td align="right">13.97</td>
    <td align="right">14.01</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.54</td>
    <td align="right">15.17</td>
    <td align="right">15.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">25.03</td>
    <td align="right">75.35</td>
    <td align="right">42.52</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">14.08</td>
    <td align="right">15.57</td>
    <td align="right">15.83</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">15.06</td>
    <td align="right">17.51</td>
    <td align="right">17.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">36.59</td>
    <td align="right">66.33</td>
    <td align="right">33.25</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">15.68</td>
    <td align="right">17.37</td>
    <td align="right">16.88</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">18.30</td>
    <td align="right">18.83</td>
    <td align="right">19.32</td>
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
    <td align="right">19.61</td>
    <td align="right">28.11</td>
    <td align="right">30.40</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">9.77</td>
    <td align="right">12.70</td>
    <td align="right">12.70</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">12.79</td>
    <td align="right">14.78</td>
    <td align="right">14.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">28.09</td>
    <td align="right">41.88</td>
    <td align="right">31.79</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">12.88</td>
    <td align="right">14.78</td>
    <td align="right">14.77</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">14.33</td>
    <td align="right">15.63</td>
    <td align="right">15.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">34.55</td>
    <td align="right">53.19</td>
    <td align="right">31.44</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">14.60</td>
    <td align="right">16.49</td>
    <td align="right">16.61</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">16.45</td>
    <td align="right">17.30</td>
    <td align="right">17.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">50.09</td>
    <td align="right">74.04</td>
    <td align="right">33.94</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">16.73</td>
    <td align="right">18.09</td>
    <td align="right">18.21</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">17.69</td>
    <td align="right">21.54</td>
    <td align="right">19.82</td>
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
    <td align="right">13.06</td>
    <td align="right">16.70</td>
    <td align="right">16.63</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.38</td>
    <td align="right">17.52</td>
    <td align="right">17.54</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.28</td>
    <td align="right">9.49</td>
    <td align="right">9.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.06</td>
    <td align="right">22.18</td>
    <td align="right">22.09</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.57</td>
    <td align="right">21.95</td>
    <td align="right">21.96</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.24</td>
    <td align="right">14.15</td>
    <td align="right">14.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">30.91</td>
    <td align="right">39.21</td>
    <td align="right">38.58</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.99</td>
    <td align="right">32.33</td>
    <td align="right">31.85</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.24</td>
    <td align="right">17.33</td>
    <td align="right">17.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">28.48</td>
    <td align="right">40.83</td>
    <td align="right">39.76</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">34.71</td>
    <td align="right">37.99</td>
    <td align="right">38.83</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">18.94</td>
    <td align="right">22.51</td>
    <td align="right">25.37</td>
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
    <td align="right">13.57</td>
    <td align="right">17.13</td>
    <td align="right">17.10</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">14.56</td>
    <td align="right">16.46</td>
    <td align="right">16.46</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">7.26</td>
    <td align="right">9.55</td>
    <td align="right">9.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">17.77</td>
    <td align="right">24.57</td>
    <td align="right">24.44</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">19.81</td>
    <td align="right">22.68</td>
    <td align="right">23.65</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">11.10</td>
    <td align="right">13.29</td>
    <td align="right">13.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">25.82</td>
    <td align="right">33.63</td>
    <td align="right">34.46</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">28.55</td>
    <td align="right">32.29</td>
    <td align="right">32.14</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">13.18</td>
    <td align="right">17.49</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">31.48</td>
    <td align="right">39.81</td>
    <td align="right">39.56</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">36.28</td>
    <td align="right">38.86</td>
    <td align="right">39.13</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">18.75</td>
    <td align="right">23.76</td>
    <td align="right">21.64</td>
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
    <td align="right">6.77</td>
    <td align="right">9.60</td>
    <td align="right">9.60</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.04</td>
    <td align="right">16.65</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.40</td>
    <td align="right">17.53</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.75</td>
    <td align="right">13.45</td>
    <td align="right">13.49</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.06</td>
    <td align="right">22.18</td>
    <td align="right">22.09</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.62</td>
    <td align="right">21.96</td>
    <td align="right">22.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">14.46</td>
    <td align="right">17.38</td>
    <td align="right">17.14</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.96</td>
    <td align="right">33.63</td>
    <td align="right">34.07</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.98</td>
    <td align="right">31.82</td>
    <td align="right">32.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">17.67</td>
    <td align="right">22.49</td>
    <td align="right">21.66</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">28.05</td>
    <td align="right">38.78</td>
    <td align="right">47.64</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">35.02</td>
    <td align="right">37.86</td>
    <td align="right">37.66</td>
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
    <td align="right">6.93</td>
    <td align="right">9.69</td>
    <td align="right">9.73</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">13.63</td>
    <td align="right">17.06</td>
    <td align="right">17.10</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">14.55</td>
    <td align="right">16.43</td>
    <td align="right">16.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">10.19</td>
    <td align="right">13.64</td>
    <td align="right">13.81</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">17.95</td>
    <td align="right">24.49</td>
    <td align="right">24.57</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">19.83</td>
    <td align="right">22.78</td>
    <td align="right">22.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">14.15</td>
    <td align="right">17.23</td>
    <td align="right">17.14</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">25.70</td>
    <td align="right">33.96</td>
    <td align="right">33.58</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">28.67</td>
    <td align="right">32.53</td>
    <td align="right">31.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">19.46</td>
    <td align="right">24.19</td>
    <td align="right">21.79</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">30.76</td>
    <td align="right">40.51</td>
    <td align="right">40.35</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">36.33</td>
    <td align="right">38.71</td>
    <td align="right">39.18</td>
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
    <td align="right">44.78</td>
    <td align="right">8.67</td>
    <td align="right">6.29</td>
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
    <td align="right">59.42</td>
    <td align="right">54.66</td>
    <td align="right">41.34</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.92</td>
    <td align="right">20.51</td>
    <td align="right">24.65</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.52</td>
    <td align="right">26.27</td>
    <td align="right">29.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.66</td>
    <td align="right">85.31</td>
    <td align="right">46.82</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">24.13</td>
    <td align="right">22.09</td>
    <td align="right">24.54</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.05</td>
    <td align="right">28.12</td>
    <td align="right">30.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.86</td>
    <td align="right">102.28</td>
    <td align="right">45.68</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.27</td>
    <td align="right">22.71</td>
    <td align="right">24.14</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.60</td>
    <td align="right">30.34</td>
    <td align="right">31.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.87</td>
    <td align="right">123.24</td>
    <td align="right">43.95</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.65</td>
    <td align="right">24.34</td>
    <td align="right">25.13</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">30.92</td>
    <td align="right">33.63</td>
    <td align="right">33.24</td>
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
    <td align="right">91.17</td>
    <td align="right">83.53</td>
    <td align="right">54.58</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">26.81</td>
    <td align="right">25.56</td>
    <td align="right">29.53</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">30.28</td>
    <td align="right">29.84</td>
    <td align="right">32.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">139.98</td>
    <td align="right">122.72</td>
    <td align="right">55.96</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">29.14</td>
    <td align="right">27.16</td>
    <td align="right">29.40</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">31.89</td>
    <td align="right">31.78</td>
    <td align="right">33.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">172.75</td>
    <td align="right">147.88</td>
    <td align="right">54.88</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">30.23</td>
    <td align="right">27.88</td>
    <td align="right">29.25</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">34.66</td>
    <td align="right">34.59</td>
    <td align="right">35.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">218.82</td>
    <td align="right">186.89</td>
    <td align="right">55.10</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">32.30</td>
    <td align="right">29.36</td>
    <td align="right">30.20</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">36.53</td>
    <td align="right">35.91</td>
    <td align="right">36.27</td>
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
    <td align="right">23.36</td>
    <td align="right">45.99</td>
    <td align="right">45.64</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.08</td>
    <td align="right">46.14</td>
    <td align="right">46.30</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.77</td>
    <td align="right">25.50</td>
    <td align="right">25.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.22</td>
    <td align="right">61.06</td>
    <td align="right">61.56</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.24</td>
    <td align="right">62.05</td>
    <td align="right">62.16</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.47</td>
    <td align="right">36.24</td>
    <td align="right">25.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.45</td>
    <td align="right">81.04</td>
    <td align="right">83.35</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.13</td>
    <td align="right">83.07</td>
    <td align="right">81.70</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.94</td>
    <td align="right">54.77</td>
    <td align="right">39.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.16</td>
    <td align="right">92.54</td>
    <td align="right">91.85</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">50.62</td>
    <td align="right">97.48</td>
    <td align="right">99.94</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.20</td>
    <td align="right">55.64</td>
    <td align="right">40.06</td>
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
    <td align="right">28.37</td>
    <td align="right">46.50</td>
    <td align="right">47.23</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">32.35</td>
    <td align="right">47.63</td>
    <td align="right">48.32</td>
    <td align="center">5</td>
    <td align="right">2.7313</td>
    <td align="right">22.66</td>
    <td align="right">26.81</td>
    <td align="right">26.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">32.55</td>
    <td align="right">62.68</td>
    <td align="right">63.07</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">39.36</td>
    <td align="right">63.73</td>
    <td align="right">64.57</td>
    <td align="center">8</td>
    <td align="right">0.5366</td>
    <td align="right">22.43</td>
    <td align="right">38.23</td>
    <td align="right">26.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">45.11</td>
    <td align="right">84.93</td>
    <td align="right">85.60</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">50.81</td>
    <td align="right">85.08</td>
    <td align="right">87.33</td>
    <td align="center">11</td>
    <td align="right">0.1134</td>
    <td align="right">31.58</td>
    <td align="right">55.88</td>
    <td align="right">39.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">48.80</td>
    <td align="right">97.26</td>
    <td align="right">96.49</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">57.11</td>
    <td align="right">100.23</td>
    <td align="right">101.30</td>
    <td align="center">13</td>
    <td align="right">0.0253</td>
    <td align="right">31.74</td>
    <td align="right">56.76</td>
    <td align="right">39.67</td>
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
    <td align="right">18.65</td>
    <td align="right">26.13</td>
    <td align="right">26.36</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.66</td>
    <td align="right">29.36</td>
    <td align="right">29.31</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.87</td>
    <td align="right">31.80</td>
    <td align="right">31.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.09</td>
    <td align="right">47.38</td>
    <td align="right">34.84</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.46</td>
    <td align="right">40.51</td>
    <td align="right">27.47</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">20.97</td>
    <td align="right">52.15</td>
    <td align="right">39.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.84</td>
    <td align="right">54.79</td>
    <td align="right">38.64</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.94</td>
    <td align="right">52.75</td>
    <td align="right">34.73</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">31.93</td>
    <td align="right">61.37</td>
    <td align="right">43.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.74</td>
    <td align="right">54.95</td>
    <td align="right">39.32</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.55</td>
    <td align="right">65.66</td>
    <td align="right">44.74</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.18</td>
    <td align="right">63.62</td>
    <td align="right">44.20</td>
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
    <td align="right">22.66</td>
    <td align="right">27.57</td>
    <td align="right">27.46</td>
    <td align="center">5</td>
    <td align="right">2.4471</td>
    <td align="right">24.09</td>
    <td align="right">29.43</td>
    <td align="right">29.33</td>
    <td align="center">5</td>
    <td align="right">2.3272</td>
    <td align="right">24.08</td>
    <td align="right">30.50</td>
    <td align="right">30.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4375</td>
    <td align="right">23.44</td>
    <td align="right">47.46</td>
    <td align="right">35.63</td>
    <td align="center">8</td>
    <td align="right">0.4137</td>
    <td align="right">23.51</td>
    <td align="right">40.02</td>
    <td align="right">27.59</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">25.04</td>
    <td align="right">54.15</td>
    <td align="right">39.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0906</td>
    <td align="right">30.85</td>
    <td align="right">55.43</td>
    <td align="right">39.42</td>
    <td align="center">11</td>
    <td align="right">0.0740</td>
    <td align="right">34.63</td>
    <td align="right">61.84</td>
    <td align="right">44.09</td>
    <td align="center">11</td>
    <td align="right">0.0604</td>
    <td align="right">34.65</td>
    <td align="right">61.83</td>
    <td align="right">43.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">31.24</td>
    <td align="right">56.07</td>
    <td align="right">40.20</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">35.03</td>
    <td align="right">65.96</td>
    <td align="right">45.33</td>
    <td align="center">14</td>
    <td align="right">0.0129</td>
    <td align="right">35.13</td>
    <td align="right">65.52</td>
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
    <td align="right">57.36</td>
    <td align="right">36.75</td>
    <td align="right">15.14</td>
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
    <td align="right">78.08</td>
    <td align="right">64.24</td>
    <td align="right">47.86</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">29.69</td>
    <td align="right">28.78</td>
    <td align="right">33.75</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">38.50</td>
    <td align="right">39.25</td>
    <td align="right">34.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">229.85</td>
    <td align="right">151.40</td>
    <td align="right">58.85</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">70.84</td>
    <td align="right">45.69</td>
    <td align="right">49.00</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">62.96</td>
    <td align="right">70.31</td>
    <td align="right">79.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">364.89</td>
    <td align="right">177.06</td>
    <td align="right">78.86</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">82.55</td>
    <td align="right">56.38</td>
    <td align="right">54.84</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">84.69</td>
    <td align="right">46.90</td>
    <td align="right">75.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">386.18</td>
    <td align="right">333.70</td>
    <td align="right">88.88</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">78.48</td>
    <td align="right">52.47</td>
    <td align="right">58.34</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">91.54</td>
    <td align="right">82.43</td>
    <td align="right">80.69</td>
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
    <td align="right">108.38</td>
    <td align="right">91.96</td>
    <td align="right">59.59</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">30.01</td>
    <td align="right">27.68</td>
    <td align="right">32.15</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">35.08</td>
    <td align="right">34.14</td>
    <td align="right">37.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">168.00</td>
    <td align="right">205.47</td>
    <td align="right">101.42</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">76.45</td>
    <td align="right">48.36</td>
    <td align="right">51.83</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">42.37</td>
    <td align="right">48.14</td>
    <td align="right">71.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">236.29</td>
    <td align="right">175.40</td>
    <td align="right">82.04</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">37.15</td>
    <td align="right">54.89</td>
    <td align="right">32.53</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">39.09</td>
    <td align="right">39.24</td>
    <td align="right">40.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">288.71</td>
    <td align="right">242.56</td>
    <td align="right">64.98</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">41.16</td>
    <td align="right">34.67</td>
    <td align="right">38.58</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">55.87</td>
    <td align="right">89.61</td>
    <td align="right">48.53</td>
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
    <td align="right">25.40</td>
    <td align="right">46.56</td>
    <td align="right">46.35</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.82</td>
    <td align="right">48.52</td>
    <td align="right">52.16</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.45</td>
    <td align="right">30.54</td>
    <td align="right">31.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">41.51</td>
    <td align="right">89.83</td>
    <td align="right">86.70</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">72.08</td>
    <td align="right">67.12</td>
    <td align="right">74.87</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">33.80</td>
    <td align="right">47.51</td>
    <td align="right">32.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">53.35</td>
    <td align="right">83.09</td>
    <td align="right">86.14</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">55.05</td>
    <td align="right">84.90</td>
    <td align="right">85.42</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">41.10</td>
    <td align="right">66.74</td>
    <td align="right">44.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">52.35</td>
    <td align="right">98.58</td>
    <td align="right">99.80</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">83.74</td>
    <td align="right">132.09</td>
    <td align="right">132.08</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">44.97</td>
    <td align="right">76.05</td>
    <td align="right">70.47</td>
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
    <td align="right">32.63</td>
    <td align="right">47.78</td>
    <td align="right">49.11</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">36.15</td>
    <td align="right">49.67</td>
    <td align="right">50.31</td>
    <td align="center">5</td>
    <td align="right">2.7250</td>
    <td align="right">24.93</td>
    <td align="right">30.18</td>
    <td align="right">29.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">34.23</td>
    <td align="right">63.45</td>
    <td align="right">63.90</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">42.45</td>
    <td align="right">64.84</td>
    <td align="right">66.20</td>
    <td align="center">8</td>
    <td align="right">0.5385</td>
    <td align="right">24.31</td>
    <td align="right">42.07</td>
    <td align="right">30.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">64.03</td>
    <td align="right">110.90</td>
    <td align="right">113.47</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">68.86</td>
    <td align="right">123.56</td>
    <td align="right">88.94</td>
    <td align="center">11</td>
    <td align="right">0.1183</td>
    <td align="right">34.72</td>
    <td align="right">61.99</td>
    <td align="right">44.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">55.60</td>
    <td align="right">103.42</td>
    <td align="right">101.77</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">66.41</td>
    <td align="right">129.60</td>
    <td align="right">111.60</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">41.55</td>
    <td align="right">69.48</td>
    <td align="right">52.01</td>
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
    <td align="right">19.77</td>
    <td align="right">30.99</td>
    <td align="right">31.20</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.63</td>
    <td align="right">33.66</td>
    <td align="right">37.73</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">28.89</td>
    <td align="right">51.40</td>
    <td align="right">56.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.07</td>
    <td align="right">50.88</td>
    <td align="right">38.65</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.15</td>
    <td align="right">43.44</td>
    <td align="right">30.32</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">22.01</td>
    <td align="right">56.12</td>
    <td align="right">43.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">32.00</td>
    <td align="right">62.06</td>
    <td align="right">45.40</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">36.01</td>
    <td align="right">56.85</td>
    <td align="right">41.11</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">35.66</td>
    <td align="right">74.40</td>
    <td align="right">57.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">77.41</td>
    <td align="right">89.16</td>
    <td align="right">52.58</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">46.07</td>
    <td align="right">114.63</td>
    <td align="right">100.77</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">38.12</td>
    <td align="right">71.67</td>
    <td align="right">51.73</td>
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
    <td align="right">24.84</td>
    <td align="right">31.63</td>
    <td align="right">31.61</td>
    <td align="center">5</td>
    <td align="right">2.4405</td>
    <td align="right">25.83</td>
    <td align="right">32.61</td>
    <td align="right">32.47</td>
    <td align="center">5</td>
    <td align="right">2.3265</td>
    <td align="right">25.96</td>
    <td align="right">45.84</td>
    <td align="right">48.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4413</td>
    <td align="right">25.50</td>
    <td align="right">84.21</td>
    <td align="right">73.22</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">24.73</td>
    <td align="right">43.03</td>
    <td align="right">29.79</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">26.50</td>
    <td align="right">58.42</td>
    <td align="right">44.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0845</td>
    <td align="right">34.33</td>
    <td align="right">60.74</td>
    <td align="right">44.17</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">36.29</td>
    <td align="right">65.99</td>
    <td align="right">48.11</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">36.24</td>
    <td align="right">67.21</td>
    <td align="right">48.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">39.52</td>
    <td align="right">66.65</td>
    <td align="right">49.12</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">40.90</td>
    <td align="right">73.14</td>
    <td align="right">52.29</td>
    <td align="center">14</td>
    <td align="right">0.0116</td>
    <td align="right">40.60</td>
    <td align="right">73.27</td>
    <td align="right">52.33</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
